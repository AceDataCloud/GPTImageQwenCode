import json
from pathlib import Path
import unittest
from urllib.parse import parse_qs, urlparse
import re

ROOT = Path(__file__).resolve().parents[1]
GPT_TOOLS = {
    'gpt_image_generate', 'gpt_image_edit', 'gpt_image_get_task',
    'gpt_image_list_tasks', 'gpt_image_list_models',
}

class ManifestTests(unittest.TestCase):
    def test_native_secret_and_service_isolation(self):
        data = json.loads((ROOT / 'qwen-extension.json').read_text())
        self.assertEqual(len(data['mcpServers']), 1)
        self.assertEqual(len(data['settings']), 1)
        secret = data['settings'][0]
        self.assertTrue(secret['sensitive'])
        server = next(iter(data['mcpServers'].values()))
        self.assertEqual(secret['envVar'], 'ACE_GPT_IMAGE_API_TOKEN')
        self.assertEqual(server['env'], {'ACEDATACLOUD_API_TOKEN': '$' + secret['envVar']})
        self.assertEqual(server['command'], 'uvx')
        self.assertEqual(server['args'], [
            '--from', 'mcp-openai-pro==2026.10.19.5',
            'mcp-openai-pro', '--profile', 'gpt-image',
        ])
        for remote_field in ['httpUrl', 'url', 'headers']:
            self.assertNotIn(remote_field, server)
        self.assertNotIn('trust', server)
        self.assertEqual(set(server['includeTools']), GPT_TOOLS)
        self.assertEqual(len(server['includeTools']), 5)
        self.assertNotIn('hooks', data)
        self.assertNotIn('workflows', data)

    def test_onboarding_links_and_artifacts(self):
        for filename in ['README.md', 'readme/README_zh_Hans.md']:
            content = (ROOT / filename).read_text()
            self.assertIn('General application', content)
            self.assertIn('task_id', content)
            self.assertIn('Python 3.10+', content)
            self.assertIn('uvx', content)
            self.assertIn('--ref v0.1.0-rc.2', content)
            self.assertIn('mcp-openai-pro==2026.10.19.5', content)
            self.assertIn('#14544', content)
            for tool in GPT_TOOLS:
                self.assertIn(tool, content)
            for url in re.findall(r'https://platform[.]acedata[.]cloud[^)\s]+', content):
                query = parse_qs(urlparse(url).query)
                self.assertEqual(set(query), {'utm_source','utm_medium','utm_campaign','utm_content'})
                self.assertEqual(query['utm_source'], ['github'])
            for image in re.findall(r'!\[[^]]*\]\(([^)]+)\)', content):
                self.assertTrue((ROOT / filename).parent.joinpath(image).resolve().is_file(), image)

    def test_release_versions_match(self):
        manifest = json.loads((ROOT / 'qwen-extension.json').read_text())
        package = json.loads((ROOT / 'package.json').read_text())
        self.assertEqual(manifest['version'], '0.1.0-rc.2')
        self.assertEqual(package['version'], manifest['version'])

    def test_commands_keep_the_dedicated_surface(self):
        instructions = (ROOT / 'QWEN.md').read_text()
        commands = '\n'.join(path.read_text() for path in (ROOT / 'commands').glob('*.md'))
        self.assertIn('gpt_image_get_task', instructions)
        self.assertIn('same ID', instructions)
        self.assertIn('gpt_image_list_models', commands)
        self.assertIn('gpt_image_get_task', commands)
        self.assertNotRegex(instructions + commands, r'\bopenai_(get_task|generate_image|list_image_models)\b')

if __name__ == '__main__':
    unittest.main()

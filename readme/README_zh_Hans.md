# GPT Image by Ace Data Cloud：Qwen Code 原生扩展

通过 Ace Data Cloud 使用 GPT Image 生成、编辑图片并查询原异步任务。独立原生扩展复用已发布的 **GPT Image 专用 stdio profile**，固定包 `mcp-openai-pro==2026.10.19.5`；不安装其他服务，也不新增 LLM Provider。

**源码预发行 `0.1.0-rc.2`。** RC1 的通用 OpenAI 远程入口与四项旧工具，现改为已发布专用五工具入口；没有新建服务器或静默回退通用入口，旧 RC1 tag 不变。源码预发行不代表 Qwen 默认市场收录或真实媒体 GA。

[English](../README.md) · [注册/登录](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=gptimageqwencode_readme_signup) · [当前价格](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=gptimageqwencode_readme_pricing)

## 1. 准备运行时并安装

安装 **Node.js 22+**、[uv](https://docs.astral.sh/uv/getting-started/installation/)（提供 `uvx`），以及可供 uv 使用的 **Python 3.10+**。包和依赖下载需要访问你批准使用的 Python 包索引。以下版本检查不需要凭据：

```bash
uvx --from mcp-openai-pro==2026.10.19.5 mcp-openai-pro --version
qwen extensions install AceDataCloud/GPTImageQwenCode --ref v0.1.0-rc.2
```

原生 manifest 启动 `uvx --from mcp-openai-pro==2026.10.19.5 mcp-openai-pro --profile gpt-image`。安装前检查本地进程与所需权限；它通过本地 stdio 与 Qwen 通信，用户选定的业务操作仍使用现有 Ace API。通用 OpenAI URL 没有独立的 GPT Image 托管 profile，下载或启动失败时不能改成那个 URL。

**真实 Token 仍须等待包含[修复 #14544](https://github.com/QwenLM/qwen-code/pull/14544) 的官方 Qwen 版本发布并复验。** 官方 0.25.2 仅为安装基线，可能无法把原生保存的敏感值展开到服务器 Header 或环境变量引用。未修复官方 CLI 只填合成占位值，不调用业务工具。源码修复候选验证不代表官方已发布；改用 stdio 不会解除该前提。

可选 [Ace 目录](https://github.com/AceDataCloud/AceDataCloudQwenCode) 在添加来源后支持 `/extensions manage` → **Discover** 搜 **GPT Image**。目录固定版本可能晚于本 RC，安装 RC2 请用上面的明确 tag；用户添加来源不等于默认官方市场收录。

## 2. 进入 General application 并取得 API Token

1. 打开 [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=gptimageqwencode_readme_api_key) 并注册/登录。需要时选择 **Initialize General Application**，再进入 **General application**。
2. 复制现有 API Key，或通过 **Manage Keys → Create** 创建独立的 `GPT Image Qwen Code` Key。
3. 检查本服务权限、有效期、用量限制、当前价格与余额。按操作限制 Allowed APIs：`/openai/images/generations`、`/openai/images/edits`、`/openai/tasks`；查询权限不代表生成权限或余额。

![复制 API Key / Manage Keys](../_assets/tutorial/get-api-key-en.png)

![创建独立 Key](../_assets/tutorial/create-api-key-en.png)

以上为固定 SunoDify 教程中 2026-10-07 的真实脱敏 Ace 应用页截图，2026-10-18 复用；展示共用应用控件，不代表本扩展实测或你的账户权益。

## 3. 在原生隐藏输入框保存 Token

满足官方修复运行时前提后，在 **Ace Data Cloud API Token** 隐藏输入框粘贴原始 API Token，不加 `Bearer` 或引号。Qwen 管理敏感凭据存储，自然选择 keychain 或加密文件。manifest 只写 `$ACE_GPT_IMAGE_API_TOKEN`，由 Qwen 展开到专用子进程的 `ACEDATACLOUD_API_TOKEN`。不要全局导出、写进参数/JSON/聊天、强制后端或解锁 Keychain 绕过故障；`platform-...` 管理 Token 不是业务 API Token。

轮换时运行下面命令，值只在随后隐藏提示框输入：

```bash
qwen extensions settings set gpt-image-by-ace-data-cloud "Ace Data Cloud API Token"
```

`qwen extensions settings list gpt-image-by-ace-data-cloud` 应遮蔽设置。重载 Qwen 并在 `/mcp` 查看状态；配置检查无需生成。已选存储缺失/不可读属于故障，应先恢复可用性并重试，考虑重装前保留可恢复的各 scope 设置。安装或连接成功，不能单独证明远端接受 Key 或拥有全部业务权限。

## 4. 核对五工具，按需明确授权业务操作

`gpt-image` 服务器仅包含：

| 工具 | 用途 |
|---|---|
| `gpt_image_generate` | 明确指定 GPT Image 模型后生成，可能计费。 |
| `gpt_image_edit` | 明确指定 GPT Image 模型后编辑，可能计费。 |
| `gpt_image_get_task` | 按原任务 `id` 查询。 |
| `gpt_image_list_tasks` | 查询有权访问的账户任务列表。 |
| `gpt_image_list_models` | 列出该 profile 的 GPT Image 模型标识。 |

专用服务器与 Qwen 精确 `includeTools` 同时限制工具范围，不暴露聊天、音频、通用 OpenAI 图片模型或退役 Sora 工具。`initialize` / `tools/list` 只发现定义，不执行这些工具；安装验证无需模型 prompt、生成或编辑。Qwen 对话模型另行配置，请模型帮忙本身也可能消耗额度。

确需媒体时，给出输入、明确允许的当前模型与预算，再授权**一次**生成或编辑。保存返回的 `task_id`，用 `gpt_image_get_task` 的 **id = 同一任务 ID** 查询。pending 时等待并查原 ID，不重生成来轮询。`finished_at` 仅表示终态，失败也会设置；检查 `response.error` / `response.success` 与可用媒体 URL 后才能报告成功。不静默切模型或自动付费重试；本文不声称付费结果或计费已验。

## 排错与隐私

- 找不到 uvx / Python 不兼容：安装运行时并重启 Qwen，使 PATH 能找到 uvx。下载失败时检查你批准的 uv 索引与网络，保留固定包和专用 profile。
- 缺少或多出工具：确认 RC2 tag/profile 参数，重启并核查同名手工 MCP 覆盖，不改通用托管入口。
- 401/403：核对原始 consumer Token、过期与 Allowed APIs；不要把 Token 放进求助日志。
- pending、429 或失败：保留响应与原任务 ID，遵守限制，不自动重发生成。

Python 包在本地运行；用户请求的媒体输入与 consumer Token 经 HTTPS 发往现有 Ace API，stdio 元数据发现本身不提交媒体任务。参见[隐私](../PRIVACY.md)、[当前价格](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=gptimageqwencode_readme_pricing)与[服务说明](https://platform.acedata.cloud/documents/openai?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=gptimageqwencode_readme_service_docs)。这是 Ace Data Cloud 集成，不冒充 GPT Image 或 Qwen 官方。

[已发布工具实现](https://github.com/AceDataCloud/OpenAIMCP) · [验证与历史](../VALIDATION.md) · [反馈](https://github.com/AceDataCloud/GPTImageQwenCode/issues) · dev@acedata.cloud。

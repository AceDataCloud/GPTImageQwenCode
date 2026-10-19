# RC2 dedicated-profile contract (2026-10-20)

RC2 replaces RC1's broad hosted endpoint/four legacy tools with the already published `mcp-openai-pro==2026.10.19.5 --profile gpt-image` stdio entry. PyPI's fixed wheel contains the dedicated five `gpt_image_*` tools and requires Python >=3.10. Qwen's declared tool filter is an exact additional allowlist, not a tool rename. No shared API/provider/billing logic is copied or changed.

Validation command: `python3 -m unittest discover -s tests -v`. It verifies the native sensitive-setting mapping into child env, exact fixed package/profile and five-tool boundary, synchronized prerelease versions, both-language onboarding links/images/runtime prerequisites and same-task guidance. Runtime installation of the new published Git tag is a separate post-publication check, recorded in the Qwen Index report; no claim is made before that check runs.

Real credentials remain restricted to a verified repair candidate or a later official fixed release. The unfixed official 0.25.2 accepts synthetic placeholders only; this transport change is not runtime GA. The earlier RC1 installed successfully but its dedicated-profile metadata was blocked. The historical four hosted-service metadata results and their partial output-log coverage stay unchanged. Before any new real-key test the execution fixture must pass synthetic late-leak/reader-completion tests. No model prompt, business tools/call, generation, billing or official marketplace acceptance is claimed.

---

The dated material below is historical RC1 validation; its hosted transport and old tool names are superseded by RC2.

# Validation (2026-10-18)

Official Qwen Code0.25.2 macOS x64; fake per-service secret and isolated profile. Native extension install, hidden prompt, manifest retained, masked setting listing, no plaintext secret in profile: PASS. Five independent packages installed from their immutable candidate GitHub archive URLs on one complete remote run; later network fetches were intermittent and local snapshots were used only for diagnosis.

Native source discovery returned all five brand entries. This is a user-added Ace catalog, not a default official Qwen listing.

BLOCKED: runtime HTTP Headers remain literal environment references even after the native secret setting is stored. Reproduced with5 localhost-only initialize connections,0 correct secret expansion; no media/model/production tools/call. Upstream issue: https://github.com/QwenLM/qwen-code/issues/14532 . No authenticated business-operation claim.

Tests: python3 -m unittest discover -s tests -v. Images are real redacted Ace Key screenshots plus a labeled official historical provider-entry edit; current extension-settings capture is queued, not forged.

## Platform follow-up


**Wait for an official Qwen release containing [fix #14544](https://github.com/QwenLM/qwen-code/pull/14544) before using this extension with a real Token.** Qwen0.25.2 is the installation baseline, not a fixed authenticated-runtime version. No fixed release version has been verified yet.

A [validation-only fork run](https://github.com/AceDataCloud/qwen-code/actions/runs/39109190158) built the owning core package at the exact fix candidate and exercised saved settings through Qwen's real MCP transport to localhost, without forcing a backend:

| Environment | Selected backend | Evidence |
|---|---|---|
| Windows Server2022 x64, Node22.23.3 | System credential store (`keychain` through keytar) | 26 checks PASS, including stored Token → extension Header → localhost initialize. This covers the hosted runner session, not every user's permission or lock state. |
| Linux x64, Node22.23.3 | Qwen's normal `encrypted_file` fallback | 25 checks PASS. The runner's system Secret Service was unavailable; this does not validate Linux Keychain. |
| macOS arm64, Node22.23.3 | Real system Keychain; follow-up 26 checks PASS | The original matrix failed at a workspace path alias. [Focused fix verification](https://github.com/AceDataCloud/qwen-code/actions/runs/39120588598) passes user/workspace/untrusted Header handshakes after canonical path identity. Fix candidate is now head6b5db858; it remains unreleased. The old matrix failure stays recorded. |

These additional Windows/Linux checks build core and use its real storage/manager/transport; they do not replace a full Windows/Linux interactive CLI test or prove a released fix. Existing macOS source-built CLI checks remain separately recorded.

The installer records the selected backend in `.qwen-extension-settings.json`; no need to copy or expose the secret bundle. Qwen can normally choose encrypted-file storage when the OS backend is unavailable; that is encrypted storage, not a plaintext Token fallback. A missing/unreadable selected store after installation is a failure, not permission to switch credentials silently. The fix candidate keeps the extension manageable and disables its MCP servers on an unreadable store. Check store availability and retry/reload first; do not uninstall for a transient lock or unavailable backend. Only after missing/corrupt settings are confirmed should you back up recoverable settings and consider reinstalling. Reinstall can preserve existing workspace overrides; review and rotate scoped settings through hidden input if needed. Do not export the Token globally, force a different backend, put it in manifests/arguments, unlock a keychain or change OS permissions to work around this candidate's blocker.

## Source prerelease boundary

Version `0.1.0-rc.1` changes only packaging/onboarding and the sensitive prompt's prerelease notice; tool list, endpoint and credential reference stay unchanged. Normal repository/tag installation is validated after publication. No production authentication, model/media generation or billing proof. Current upstream head77b2196 platform evidence: https://github.com/AceDataCloud/qwen-code/actions/runs/39142135018 .

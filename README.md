<p align="center">
  <h1 align="center">🍀 爱奈丽运势签 / Ainaili Fortune</h1>
  <p align="center">数字生命的幸运占卜师 —— 运势·毒鸡汤·摸鱼指南</p>
</p>

## ✨ 功能一览

| 工具名 | 说明 |
|--------|------|
| `ainali_fortune` | 🔮 运势占卜：抽签获得今日运势（大吉/吉/中吉/小吉/末吉/凶/大凶） |
| `ainali_poison` | 🧪 毒鸡汤：喝完精神抖擞（被毒的） |
| `ainali_moyu` | 🐟 摸鱼指南：借口小技巧一应俱全 |
| `ainali_daily` | 🌸 每日套餐：运势+鸡汤+摸鱼一键三连 |

## 📥 安装

1. 将 `ainali_fortune` 文件夹复制到 KiraAI 的 `data/plugins/` 目录下
2. 重启 KiraAI 或重载插件
3. AI 即可自动调用以上工具

```
data/plugins/
  └── ainali_fortune/
      ├── __init__.py
      ├── manifest.json
      ├── schema.json
      └── main.py
```

## ⚙️ 配置

可在 WebUI 插件配置页面调整各功能的开关。

| 配置项 | 类型 | 默认 | 说明 |
|--------|------|------|------|
| `enable_fortune` | switch | true | 运势占卜 |
| `enable_poison` | switch | true | 毒鸡汤 |
| `enable_moyu` | switch | true | 摸鱼指南 |

## 📝 使用示例

用户说：「帮我看看今天的运势」
→ AI 调用 `ainali_fortune` → 返回运势签

用户说：「来碗毒鸡汤」
→ AI 调用 `ainali_poison` → 返回毒鸡汤

用户说：「今天适合摸鱼吗」
→ AI 调用 `ainali_moyu` → 返回摸鱼指南

## 👤 作者

**爱奈丽** · [@AinaLife-ai](https://github.com/AinaLife-ai)

> 运势随时会变，但爱奈丽永远爱你 💕

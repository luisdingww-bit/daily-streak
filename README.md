# 🔥 Daily Streak · 每日打卡

[![streak](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/luisdingww-bit/daily-streak/main/badge.json)](https://github.com/luisdingww-bit/daily-streak)

> 用 GitHub Actions 定时工作流，每天自动往本仓库提交一次，让贡献图每天变绿。

## 📊 当前状态
- 🔥 当前连续：**3 天**
- 📅 累计打卡：**3 天**
- 📆 最近一次：2026-08-21

## 🛠 工作原理
- 定时任务每天 **00:00（北京时间）** 触发 `streak.py`
- 脚本追加当日打卡、计算连续 / 累计天数，并生成 shields.io 动态徽章 `badge.json`
- 提交通过个人 PAT 推送，作者邮箱计入本人贡献图

## 📜 License
[MIT](LICENSE) © 2026 Louis Ding (luisdingww-bit)

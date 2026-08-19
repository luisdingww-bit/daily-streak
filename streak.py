import re, os, json
from datetime import datetime, timedelta

try:
    from zoneinfo import ZoneInfo
    tz = ZoneInfo("Asia/Shanghai")
except Exception:
    tz = None

now = datetime.now(tz) if tz else (datetime.utcnow() + timedelta(hours=8))
today = now.strftime("%Y-%m-%d")
stamp = now.strftime("%Y-%m-%d %H:%M:%S") + " CST"

path = "streak.md"
log_lines = []
if os.path.exists(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.rstrip("\n")
            if re.match(r"^- \d{4}-\d{2}-\d{2}", s):
                log_lines.append(s)

dates = [re.match(r"^- (\d{4}-\d{2}-\d{2})", l).group(1) for l in log_lines]
if today not in dates:
    log_lines.append(f"- {stamp} — 每日打卡")
    dates.append(today)

udates = sorted(set(dates))
dset = set(udates)
maxd = max(udates)
cur = datetime.strptime(maxd, "%Y-%m-%d").date()
streak = 0
while cur.strftime("%Y-%m-%d") in dset:
    streak += 1
    cur -= timedelta(days=1)
cumulative = len(udates)

# streak.md
out = []
out.append("# Daily Streak · 每日打卡")
out.append("")
out.append(f"- 🔥 当前连续：**{streak} 天**")
out.append(f"- 📅 累计打卡：**{cumulative} 天**")
out.append(f"- 📆 最近一次：{maxd}")
out.append("")
out.append("## 打卡记录")
for l in log_lines:
    out.append(l)
out.append("")
with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(out))

# badge.json (shields.io endpoint)
badge = {
    "schemaVersion": 1,
    "label": "连续打卡",
    "message": f"{streak} 天 · 累计 {cumulative} 天",
    "color": "ff4757",
}
with open("badge.json", "w", encoding="utf-8") as f:
    json.dump(badge, f, ensure_ascii=False)

# README.md
readme = f"""# 🔥 Daily Streak · 每日打卡

[![streak](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/luisdingww-bit/daily-streak/main/badge.json)](https://github.com/luisdingww-bit/daily-streak)

> 用 GitHub Actions 定时工作流，每天自动往本仓库提交一次，让贡献图每天变绿。

## 📊 当前状态
- 🔥 当前连续：**{streak} 天**
- 📅 累计打卡：**{cumulative} 天**
- 📆 最近一次：{maxd}

## 🛠 工作原理
- 定时任务每天 **00:00（北京时间）** 触发 `streak.py`
- 脚本追加当日打卡、计算连续 / 累计天数，并生成 shields.io 动态徽章 `badge.json`
- 提交通过个人 PAT 推送，作者邮箱计入本人贡献图

## 📜 License
[MIT](LICENSE) © 2026 Louis Ding (luisdingww-bit)
"""
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print(f"streak={streak} cumulative={cumulative}")

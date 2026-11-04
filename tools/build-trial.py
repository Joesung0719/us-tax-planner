#!/usr/bin/env python3
"""由 index.html 產生測試版 trial/app.html,正式版不動。正式版改過後重跑一次再推上去。

用法: python3 tools/build-trial.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
html = (ROOT / "index.html").read_text(encoding="utf-8")

def sub(old, new):
    global html
    assert html.count(old) >= 1, f"找不到:{old[:40]}"
    html = html.replace(old, new)

# 1) 到期檢查:過期(或讀不到到期設定)就回到 ./ 顯示到期訊息,不載入試算內容
guard = ('<meta name="robots" content="noindex,nofollow">'
         '<script src="/us-tax-planner/trial/expiry.js"></script>'
         '<script>if(!window.TRIAL||TRIAL.expired)location.replace("./"+location.hash);</script>')
sub("<head>", "<head>" + guard)
sub("<title>美國稅務試算</title>", "<title>美國稅務試算(測試版)</title>")

# 2) 頂端測試版橫幅
banner = ('<div id="trialBanner" style="background:#fef3c7;border-bottom:2px solid #f59e0b;color:#78350f;'
          'font-size:1rem;line-height:1.6;padding:10px 14px;text-align:center">'
          '<b>測試版</b>,試用至 <b id="trialEnd"></b><span id="trialLeft"></span>。數字為示意估算,不構成投資、法律或稅務建議。'
          '所有計算都在你的瀏覽器內完成,不會上傳你輸入的資料。</div>'
          '<script>document.getElementById("trialEnd").textContent=TRIAL.expires;'
          'document.getElementById("trialLeft").textContent="(剩 "+TRIAL.daysLeft+" 天)";</script>')
sub('<body data-mode="nra">', '<body data-mode="nra">' + banner)

# 3) 連到台灣退休與傳承試算的測試版,不連正式版
sub("https://joesung0719.github.io/cfp-planner/", "https://joesung0719.github.io/cfp-planner/trial/")

(ROOT / "trial" / "app.html").write_text(html, encoding="utf-8")
print("OK trial/app.html")

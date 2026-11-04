# 美國稅務計劃

美國稅務試算頁面:第一階段 非美國人(例如在美有資產的台灣人)、第二階段 綠卡持有者、第三階段 美國公民。在「身分判定」分頁切換身分,其他分頁內容跟著切換。單一 `index.html`,無需建置,可直接用 GitHub Pages 發佈。

- 查證紀錄與待確認清單:`docs/查證筆記-第一階段.md`、`docs/查證筆記-第二階段-綠卡.md`、`docs/查證筆記-第三階段-美國公民.md`
- 法定數值(稅率表、$13,000 抵免、$60,000 門檻)集中在 `index.html` 內的 `BRACKETS`(§2001(c))與 `Y2026`(Rev. Proc. 2025-32)。每年 11 月、1 月重新核對。
- 規則:數字須對照 IRS / IRC 原文;未驗證標「待確認」。

不構成投資、法律或稅務建議。

## 測試版(給保戶試用,限期)

- 網址:`https://joesung0719.github.io/us-tax-planner/trial/`(搭配台灣退休與傳承試算的試用版 `https://joesung0719.github.io/cfp-planner/trial/`,兩邊互相連結)。
- **到期日只改一處**:`trial/expiry.js` 的 `TRIAL_EXPIRES = "YYYY-MM-DD"`(台灣時間當天 23:59:59 止)。兩個試用版共用這個檔,改了推上 main 即一起生效。
- 到期後 `trial/` 只顯示「試用期已結束,請聯絡 Joe」,不會轉到試算內容;直接開 `trial/app.html` 也會被轉回。
- 這是前端軟性限制:GitHub Pages 是純靜態,懂技術的人可改電腦時間或直接讀原始碼繞過;正式版網址本身也是公開的。要硬性關閉,刪掉 `trial/` 資料夾(或只刪 `trial/app.html`)並推上 main,幾分鐘後該網址就是 404。
- 正式版 `index.html` 改過後,跑 `python3 tools/build-trial.py` 重新產生 `trial/app.html` 再推上去,測試版才會跟著更新。
- 本頁沒有任何資料上傳;輸入只在保戶自己的瀏覽器內計算。
- 「客戶資料」儲存:存在該台電腦瀏覽器的 localStorage,不上傳。正式版鍵 `usTaxPlanner.clients.v1`,測試版由 build-trial.py 自動改成 `usTaxPlanner.trial.clients.v1`,兩者分開。

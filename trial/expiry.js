// ===== 測試版到期設定(美國稅務試算、台灣退休與傳承試算兩個測試版共用) =====
// 只要改下面這一行日期,兩個測試版就一起改。格式 YYYY-MM-DD,以台灣時間當天 23:59:59 為止。
var TRIAL_EXPIRES = "2026-11-18";
// 到期後顯示的聯絡說明
var TRIAL_CONTACT = "如需繼續使用,請聯絡提供此連結給你的 Joe。";

(function () {
  var end = new Date(TRIAL_EXPIRES + "T23:59:59+08:00").getTime();
  // 以台灣日期計算還剩幾天(例:11/04 到 11/18 = 剩 14 天;到期當天顯示「今天最後一天」)
  var todayTW = new Date(Date.now() + 8 * 3600000).toISOString().slice(0, 10);
  var left = Math.round((Date.parse(TRIAL_EXPIRES) - Date.parse(todayTW)) / 86400000);
  window.TRIAL = { expires: TRIAL_EXPIRES, contact: TRIAL_CONTACT, end: end, daysLeft: left,
    daysText: left > 0 ? "剩 " + left + " 天" : "今天最後一天", expired: !(Date.now() <= end) };
})();

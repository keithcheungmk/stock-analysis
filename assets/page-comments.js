/**
 * Page comments for GitHub Pages.
 * Stores notes as public GitHub Issues titled "[頁面意見] …".
 * Agents pick those up with: gh issue list --search "[頁面意見]"
 */
(function () {
  const REPO = "keithcheungmk/stock-analysis";
  const mount = document.getElementById("page-comments");
  if (!mount) return;

  const page =
    mount.getAttribute("data-page") ||
    (location.pathname.split("/stock-analysis")[1] || location.pathname);

  const title = "[頁面意見] " + (document.title || page) + " · " + page;
  const issueBody =
    "頁面：" +
    location.href +
    "\n路徑：" +
    page +
    "\n\n我嘅意見：\n";
  const newIssue =
    "https://github.com/" +
    REPO +
    "/issues/new?title=" +
    encodeURIComponent(title) +
    "&body=" +
    encodeURIComponent(issueBody);

  mount.innerHTML =
    '<div class="pc-box">' +
    "<h2>頁面意見</h2>" +
    "<p>喺呢度留言，下次分析會跟住改。唔使睇任何程式碼。</p>" +
    '<a class="pc-btn" href="' +
    newIssue +
    '">寫意見</a>' +
    '<div class="pc-list" id="pc-list">載入緊現有意見…</div>' +
    "</div>";

  const style = document.createElement("style");
  style.textContent = [
    "#page-comments{margin:28px 12px 40px;font-family:Manrope,PingFang TC,sans-serif}",
    ".pc-box{max-width:720px;margin:0 auto;background:#fff;border:1px solid #d7dee7;border-radius:18px;padding:18px}",
    ".pc-box h2{margin:0 0 6px;font-size:1.05rem;color:#0b1f33}",
    ".pc-box p{margin:0 0 12px;color:#5b6b7c;font-size:.88rem}",
    ".pc-btn{display:inline-block;background:#0e7c66;color:#fff;text-decoration:none;font-weight:800;padding:10px 16px;border-radius:999px}",
    ".pc-list{margin-top:14px}",
    ".pc-item{border-top:1px solid #e8edf3;padding:10px 0}",
    ".pc-item a{color:#1d4ed8;font-weight:700;text-decoration:none}",
    ".pc-meta{color:#5b6b7c;font-size:.75rem;margin-top:4px}",
    ".pc-empty{color:#5b6b7c;font-size:.82rem}",
  ].join("");
  document.head.appendChild(style);

  const list = document.getElementById("pc-list");
  const api =
    "https://api.github.com/search/issues?q=" +
    encodeURIComponent("repo:" + REPO + " is:issue [頁面意見] in:title") +
    "&sort=updated";

  fetch(api)
    .then(function (r) {
      return r.json();
    })
    .then(function (data) {
      const items = (data.items || []).filter(function (it) {
        return (it.title || "").indexOf(page) !== -1;
      });
      if (!items.length) {
        list.innerHTML = '<p class="pc-empty">呢頁暫時未有意見。</p>';
        return;
      }
      list.innerHTML = items
        .slice(0, 8)
        .map(function (it) {
          const when = (it.updated_at || "").slice(0, 10);
          const state = it.state === "closed" ? "已處理" : "待處理";
          return (
            '<div class="pc-item"><a href="' +
            it.html_url +
            '">' +
            it.title.replace("[頁面意見] ", "") +
            "</a><div class=\"pc-meta\">" +
            state +
            " · " +
            when +
            "</div></div>"
          );
        })
        .join("");
    })
    .catch(function () {
      list.innerHTML =
        '<p class="pc-empty">暫時載入唔到意見列表。你仍然可以撳「寫意見」。</p>';
    });
})();

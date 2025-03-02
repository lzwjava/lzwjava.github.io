---
audio: false
generated: true
lang: hant
layout: post
title: 常見的 HTTP 回應碼
translated: true
---

你有沒有在瀏覽網頁時遇到過「404 Not Found」錯誤，並好奇它的意思？或者你可能遇到過「500 Internal Server Error」，並對它為什麼會出現感到困惑。這些數字是**HTTP 回應碼**，它們是網際網路溝通的關鍵角色。在這篇部落格中，我們將解釋這些碼的含義，探討一些最常見的碼，並解釋為什麼了解它們對開發者或好奇的網頁使用者都很重要。

---

## 什麼是 HTTP？

讓我們從基礎開始。**HTTP**，或*超文本傳輸協議*，是驅動世界廣域網數據交換的系統。當你在瀏覽器中輸入 URL 並按下 Enter 鍵時，你的瀏覽器會向托管該網站的伺服器發送一個**HTTP 要求**。伺服器然後用一個包含三位數**狀態碼**的**HTTP 回應**作為回應。這個碼告訴你你的要求是否成功，如果沒有，告訴你出了什麼問題。

---

## HTTP 回應碼的五個類別

HTTP 回應碼分為五個類別，每個類別都有特定的用途：

- **1xx（資訊）**：伺服器收到你的要求並正在處理中。
- **2xx（成功）**：你的要求已被接收、理解並成功完成。
- **3xx（重新導向）**：你需要多做一步，例如遵循新的 URL，才能得到你想要的。
- **4xx（客戶端錯誤）**：你這邊出了問題，例如拼寫錯誤或缺少憑證。
- **5xx（伺服器錯誤）**：伺服器遇到問題無法處理你的有效要求。

現在，讓我們深入探討你最有可能遇到的碼。

---

## 常見 HTTP 回應碼解釋

以下是最常見的 HTTP 回應碼，並附上範例以便理解：

### 200 OK
- **意義**：要求成功。伺服器處理了它並返回你要求的數據。
- **範例**：加載網頁如 `www.example.com` 而沒有問題？那就是 200 OK。

### 201 Created
- **意義**：你的要求成功，並且創建了一個新資源。
- **範例**：提交表單訂閱新聞，伺服器確認你的帳戶已創建。

### 301 Moved Permanently
- **意義**：你想要的資源已永久移動到新的 URL，你應該從現在開始使用新地址。
- **範例**：部落格文章從 `oldblog.com/post1` 移動到 `newblog.com/post1`，伺服器將你重新導向。

### 302 Found
- **意義**：資源暫時在不同的 URL，但你應該繼續使用原始 URL 進行未來的要求。
- **範例**：網站的首頁暫時重新導向到節日促銷頁面。

### 404 Not Found
- **意義**：伺服器找不到你要的東西——可能頁面已經消失或 URL 錯誤。
- **範例**：輸入 `www.example.com/oops` 並進入錯誤頁面，因為「oops」不存在。

### 403 Forbidden
- **意義**：伺服器知道你想要什麼，但不讓你得到它，因為你沒有權限。
- **範例**：嘗試在未登錄的情況下訪問私人管理面板。

### 401 Unauthorized
- **意義**：你需要進行身份驗證（例如登錄）才能繼續。
- **範例**：訪問會員專屬論壇而未先登錄。

### 400 Bad Request
- **意義**：伺服器無法理解你的要求，因為語法錯誤或無效數據。
- **範例**：提交一個電子郵件欄位為亂碼的表單，例如「@#$%」。

### 500 Internal Server Error
- **意義**：伺服器端出了問題，但它沒告訴你是什麼。
- **範例**：網站因開發者未發現的錯誤而崩潰。

### 503 Service Unavailable
- **意義**：伺服器已關閉——可能是進行維護或因過載。
- **範例**：嘗試在大促銷期間購物，但看到「稍後再試」的訊息。

---

## 幾個值得了解的其他碼

這些碼不如常見，但出現頻率足夠高，值得一提：

- **100 Continue**：伺服器同意你發送大要求，所以繼續。
- **204 No Content**：要求成功，但沒有要返回的內容（例如在刪除後）。
- **304 Not Modified**：資源沒有變化，所以使用你已經有的快取版本。
- **429 Too Many Requests**：你請求得太頻繁，伺服器告訴你冷靜一下（在 API 中很常見）。
- **502 Bad Gateway**：中間伺服器從它試圖到達的主要伺服器收到錯誤回應。

---

## HTTP 碼的日常類比

讓我們用一些現實生活中的比較來使這些碼更具關聯性：

- **200 OK**：你點了一杯咖啡，它被正確地交給你。
- **201 Created**：你要求一件定制 T 恤，商店說「正在製作中！」
- **301 Moved Permanently**：你常去的餐廳搬到了鎮的另一邊並給了你新地址。
- **302 Found**：餐廳因維修關閉，但他們指引你到附近的食品車。
- **404 Not Found**：你在圖書館要求一本書，但它不在他們的目錄中。
- **403 Forbidden**：你嘗試參加沒有邀請的私人派對。
- **401 Unauthorized**：你嘗試使用健身房但忘了會員卡。
- **400 Bad Request**：你用服務員不理解的語言點餐。
- **500 Internal Server Error**：你向廚師要求湯，廚房著火了。
- **503 Service Unavailable**：你打電話給熱線，但所有線路都忙。

---

## 為什麼要關心 HTTP 碼？

對於**開發者**，這些碼是無價的。它們幫助你調試問題、優雅地處理錯誤，並構建不會讓用戶掛起來的應用程序。例如，知道是 400 還是 500 錯誤發生，可以確定問題是出在用戶還是伺服器。

對於**普通用戶**，對這些碼的基本了解可以解開網頁故障的謎團。404 表示頁面丟失，而 503 表示等待。這就像有一張網際網路的作弊手冊。

此外，**搜尋引擎**依賴這些碼進行 SEO。301 重新導向可以在你移動內容時保留你的網站排名，而 404 可能會向 Google 發出死胡同的信號。

---

## 總結

HTTP 回應碼是網頁與我們溝通的方式，告訴我們我們的要求是否成功或失敗。從勝利的 **200 OK** 到可怕的 **500 Internal Server Error**，每個碼都講述了一個故事。無論你是編碼網站還是只是瀏覽，了解這些常見的碼可以使你的網上生活更順暢和不神秘。所以下次你看到 404，你會知道不是你——只是網頁說「我找不到那個頁面！」
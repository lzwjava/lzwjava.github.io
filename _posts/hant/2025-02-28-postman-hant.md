---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Postman 功能
translated: true
---

Postman 是一個廣泛使用的 **API 開發和測試平台**，簡化了構建、測試和文檔化 API 的過程。它提供了一個用戶友好的介面和一套強大的工具，支持各種協議，包括 **HTTP、REST、GraphQL、WebSockets 等**。無論你是獨自工作還是與團隊合作，Postman 提供了實時協作、自動化測試和環境管理等功能，以簡化你的 API 工作流程。本指南將帶你了解 Postman 的關鍵功能，並提供如何有效使用它們的逐步指示。

---

### Postman 的關鍵功能

Postman 提供了各種功能，旨在使 API 開發更加簡單和高效：

- **請求構建**：輕鬆創建和發送 HTTP 請求。
- **集合管理**：將請求組織到集合中以便更好地管理。
- **環境變量**：管理不同環境（例如開發、測試、生產）的配置。
- **驗證**：無縫處理各種驗證方法。
- **測試**：編寫和運行測試以驗證 API 响應。
- **模擬**：模擬 API 响應以進行測試。
- **文檔**：自動生成和共享 API 文檔。
- **協作**：與團隊成員共享集合和環境。

下面，我們將詳細探討每個功能。

---

### 1. **請求構建**
請求構建是 Postman 的核心功能，允許你輕鬆創建和發送 HTTP 請求。

- **如何使用**：
  - 打開 Postman 並點擊 **新建** > **請求**。
  - 從下拉菜單中選擇 HTTP 方法（例如 `GET`、`POST`、`PUT`、`DELETE`）。
  - 在地址欄中輸入 API 端點 URL（例如 `https://api.example.com/users`）。
  - 在 **標頭** 選項卡中添加標頭（例如 `Content-Type: application/json`）。
  - 對於 `POST` 或 `PUT` 方法，在 **主體** 選項卡中添加請求主體（選擇格式，例如 `JSON`、`form-data` 等）。
  - 點擊 **發送** 以執行請求並在下方窗格中查看響應。

- **提示**：使用 **參數** 選項卡為 `GET` 請求添加查詢參數（例如 `?id=123`）到你的 URL。

---

### 2. **集合管理**
集合幫助你組織相關請求，使得管理和運行多個請求變得更加容易。

- **如何使用**：
  - 點擊 **新建** > **集合** 以創建新集合。
  - 為集合命名（例如 "用戶 API"）並添加可選描述。
  - 通過從側邊欄拖放或在集合內點擊 **添加請求** 將請求添加到集合中。
  - 要運行整個集合，點擊集合名稱旁的 **...** 並選擇 **運行集合**。這將打開 **集合運行器**，你可以在其中順序或並行執行所有請求。

- **提示**：在集合中使用文件夾進一步按功能組織請求（例如 "驗證"、"用戶管理"）。

---

### 3. **環境變量**
環境變量允許你管理不同環境（例如基礎 URL、API 密鑰）的配置，而無需手動更改每個請求。

- **如何使用**：
  - 點擊右上角的 **眼睛** 圖標打開 **環境管理器**。
  - 點擊 **添加** 以創建新環境（例如 "開發"、"生產"）。
  - 為每個環境定義鍵值對（例如 `base_url: https://api.example.com`）。
  - 在請求中，使用雙大括號將變量包裹起來，例如 `{{base_url}}/users`。
  - 通過從右上角的下拉菜單選擇所需的環境來切換環境。

- **提示**：使用 **全局變量** 來保存跨環境保持不變的值，例如 API 密鑰。

---

### 4. **驗證**
Postman 簡化了處理各種驗證方法，確保安全訪問你的 API。

- **如何使用**：
  - 在請求選項卡中，轉到 **授權** 選項卡。
  - 從下拉菜單中選擇驗證類型（例如 **基本驗證**、**Bearer 令牌**、**OAuth 2.0**、**API 密鑰**）。
  - 填寫所需的憑據或令牌（例如基本驗證的用戶名和密碼，或 Bearer 令牌的令牌）。
  - Postman 將自動將驗證詳細信息添加到請求標頭中。

- **示例**：
  - 對於 **Bearer 令牌**，粘貼你的令牌，Postman 將在 `Authorization` 標頭中包含它作為 `Bearer <token>`。

---

### 5. **測試**
Postman 的測試框架允許你編寫 JavaScript 測試以驗證 API 响應，確保你的 API 正常工作。

- **如何使用**：
  - 在請求選項卡中，轉到 **測試** 選項卡。
  - 編寫 JavaScript 代碼以驗證響應。例如：
    ```javascript
    pm.test("狀態碼是 200", function () {
        pm.response.to.have.status(200);
    });
    ```
  - 發送請求後，檢查響應窗格中的 **測試結果** 以查看測試是否通過或失敗。

- **提示**：使用 Postman 的內置代碼片段（例如 "狀態碼是 200"、"響應主體：JSON 值檢查"）快速添加常見測試。

---

### 6. **模擬**
模擬允許你模擬 API 响應，這在實際 API 仍在開發或不可用時非常有用。

- **如何使用**：
  - 創建新集合或使用現有集合。
  - 點擊集合旁的 **...** 並選擇 **模擬集合**。
  - 為集合中的每個請求定義模擬響應（例如樣本 JSON 數據）。
  - Postman 將生成一個模擬服務器 URL（例如 `https://<mock-id>.mock.pstmn.io`），你可以用它發送請求並接收模擬響應。

- **提示**：使用模擬使前端開發人員能夠獨立工作，而無需等待後端準備就緒。

---

### 7. **文檔**
Postman 可以根據集合中的請求自動生成 API 文檔。

- **如何使用**：
  - 打開集合並點擊 **...** 圖標。
  - 選擇 **查看文檔** 以生成文檔頁面。
  - 通過添加描述、示例和標籤來自定義文檔。
  - 通過將其發布為公共文檔或與團隊共享鏈接來共享文檔。

- **提示**：通過與集合更改同步來保持文檔的最新狀態。

---

### 8. **協作**
Postman 的協作功能使團隊能夠高效地在 API 專案上合作。

- **如何使用**：
  - 通過點擊 **工作區** > **創建工作區** 創建 **團隊工作區**。
  - 通過電子郵件或鏈接邀請團隊成員加入工作區。
  - 在工作區內共享集合、環境和其他資源。
  - 使用 **版本控制** 來分叉集合、進行更改並通過拉取請求合併更新。

- **提示**：在請求或集合上使用 **評論** 討論更改並直接在 Postman 中提供反饋。

---

### 使用 Postman 的其他技巧

- **使用腳本**：利用 **請求前腳本** 在發送請求之前設置數據或條件（例如生成時間戳）。
- **監控 API**：設置 **監控器** 以按計劃間隔運行集合並檢查 API 健康狀況或可用性。
- **與 CI/CD 集成**：使用 **Newman**，Postman 的命令行工具，在 CI/CD 管道中運行集合（例如 Jenkins、GitHub Actions）。
- **探索 Postman 流**：使用 **流** 可視化構建和自動化複雜 API 工作流，而無需編寫代碼。
- **保護敏感數據**：將敏感信息（例如 API 密鑰）存儲在 **Postman Vault** 中以安全訪問。

---

### 結論

Postman 是一個強大的平台，超越了簡單的 API 測試，提供了一套全面的工具來進行 API 開發、協作和自動化。通過掌握請求構建、環境管理、測試和模擬等功能，你可以顯著提高生產力並簡化 API 工作流程。無論你是獨立開發人員還是大型團隊的一員，Postman 的直觀介面和先進功能使其成為現代 API 開發的必備工具。立即開始探索這些功能，發揮你的 API 專案的最大潛力！
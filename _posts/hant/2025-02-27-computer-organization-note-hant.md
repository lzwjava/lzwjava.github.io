---
audio: false
generated: true
lang: hant
layout: post
title: 電腦組織 - 筆記
translated: true
---

半導體記憶體是一種使用半導體電路作為存儲介質的存儲設備。它由稱為記憶體芯片的半導體整合電路組成。根據其功能，半導體記憶體可以分為兩大類：隨機存取記憶體（RAM）和唯讀記憶體（ROM）。

- **隨機存取記憶體（RAM）**：這種記憶體允許在任何時候以任何順序讀取和寫入數據。它用於暫時存儲CPU可能需要快速訪問的數據。RAM是易失性的，這意味著它需要電源來維持存儲的信息；一旦電源關閉，數據就會丟失。

- **唯讀記憶體（ROM）**：這種記憶體用於永久存儲在系統運行期間不變或變化非常少的數據。ROM是非易失性的，這意味著它在電源關閉時仍然保留其數據。

通過隨機存取方法訪問存儲在半導體記憶體中的信息，這允許從記憶體的任何位置快速檢索數據。這種方法提供了幾個優點：

1. **高存儲速度**：數據可以快速訪問，因為可以直接訪問任何記憶體位置，而不需要通過其他位置。

2. **高存儲密度**：半導體記憶體可以在相對較小的物理空間中存儲大量數據，使其適合用於現代電子設備。

3. **易於與邏輯電路接口**：半導體記憶體可以輕鬆與邏輯電路集成，使其適合用於複雜的電子系統。

這些特性使半導體記憶體成為現代計算和電子設備中的關鍵組件。

---

堆疊指針（SP）是一個8位特殊用途寄存器，指示堆疊的頂部元素的地址，具體來說是堆疊頂部在內部RAM塊中的位置。這由堆疊設計者決定。在硬件堆疊機中，堆疊是計算機用來存儲數據的數據結構。SP的作用是指向當前被推入或彈出堆疊的數據，並在每次操作後自動增量或減量。

然而，有一個具體的細節需要注意：在這種情況下，當數據被推入堆疊時，SP會增量。SP在推操作中是否增量或減量由CPU製造商決定。通常，堆疊由一個存儲區和一個指向該存儲區的指針（SP）組成。

總結來說，SP對於通過跟蹤堆疊的當前頂部並隨著數據被推入或彈出堆疊而調整其值來管理堆疊是至關重要的，具體行為（增量或減量）是CPU製造商做出的設計選擇。

---

讓我們分解CPU中的狀態寄存器、程序計數器和數據寄存器的角色：

1. **狀態寄存器**：
   - **用途**：狀態寄存器，也稱為狀態寄存器或標誌寄存器，保存CPU的當前狀態信息。它包含指示算術和邏輯操作結果的標誌。
   - **標誌**：常見的標誌包括零標誌（指示結果為零）、進位標誌（指示最有意義的位的進位）、符號標誌（指示負結果）和溢出標誌（指示算術溢出）。
   - **角色**：狀態寄存器有助於CPU內的決策過程，例如基於先前操作結果的條件分支。

2. **程序計數器（PC）**：
   - **用途**：程序計數器是一個寄存器，保存下一條要執行的指令的地址。
   - **角色**：它跟蹤指令序列，確保指令按正確順序提取和執行。在提取指令後，程序計數器通常會增量以指向下一條指令。
   - **控制流**：程序計數器對於管理程序執行流程至關重要，包括處理分支、跳轉和函數調用。

3. **數據寄存器**：
   - **用途**：數據寄存器用於暫時保存CPU當前正在處理的數據。
   - **類型**：有各種類型的數據寄存器，包括通用寄存器（用於各種數據操作任務）和特殊用途寄存器（用於特定功能，如累加器）。
   - **角色**：數據寄存器促進了數據處理過程中的快速訪問，減少了訪問較慢的主存儲的需求。它們對於高效地執行算術、邏輯和其他數據操作任務至關重要。

每個這些寄存器在CPU的操作中都起著關鍵作用，使其能夠執行指令、管理數據並有效地控制程序流程。

---

微程序是一個存儲在控制存儲（通常是一種唯讀記憶體，或ROM）中的低級程序，用於實現處理器的指令集。它由微指令組成，這些微指令是詳細的、逐步的命令，指示處理器的控制單元執行特定操作。

這裡是概念的分解：

- **微指令**：這些是微程序中的單個命令。每個微指令指定處理器應該執行的特定操作，例如在寄存器之間移動數據、執行算術操作或控制執行流程。

- **控制存儲**：微程序存儲在一個稱為控制存儲的特殊存儲區中，這通常是使用ROM實現的。這確保了微程序在正常操作期間永遠可用且不可更改。

- **指令實現**：微程序用於實現處理器的機器級指令。當處理器從存儲器提取指令時，它使用相應的微程序來執行該指令，將其分解為一系列微指令。

- **靈活性和效率**：使用微程序使處理器設計更加靈活，因為可以通過修改微程序來更改指令集，而不是硬件本身。這種方法還能通過優化每條指令的操作序列來更有效地利用硬件資源。

總結來說，微程序在處理器的操作中起著關鍵作用，通過在專用控制存儲區中提供每條機器級指令的詳細、逐步實現。

---

平行接口是一種接口標準，其中數據在兩個連接的設備之間以平行方式傳輸。這意味著多個數據位同時通過單獨的線路傳輸，而不是像串行通信那樣一位一位地傳輸。

這裡是平行接口的關鍵方面：

- **平行傳輸**：在平行接口中，數據通過多個通道或線路同時傳輸。每個數據位都有自己的線路，這使得數據傳輸速度比串行傳輸快。

- **數據寬度**：平行接口中的數據通道寬度指的是可以同時傳輸的位數。常見的寬度是8位（一個字節）或16位（兩個字節），但根據具體接口標準，其他寬度也是可能的。

- **效率**：平行接口可以實現高數據傳輸速率，因為多個位同時傳輸。這使它們適合於速度至關重要的應用，例如某些類型的計算機總線和較舊的打印機接口。

- **複雜性**：儘管平行接口提供速度優勢，但它們可能更複雜和昂貴，因為需要多個數據線和它們之間的同步。它們也更容易受到干擾和偏差的影響，這些問題可能會影響高速下的數據完整性。

總結來說，平行接口通過同時通過單獨線路傳輸多個數據位來實現快速數據傳輸，數據寬度通常以字節為單位。

---

中斷掩碼是一種機制，用於暫時禁用或“掩碼”某些中斷，防止它們被CPU處理。這裡是它的工作原理：

- **用途**：中斷掩碼允許系統選擇性地忽略或延遲處理特定的中斷請求。這在某些操作需要在沒有中斷的情況下完成，或當更高優先級的任務需要優先處理時非常有用。

- **功能**：當中斷被掩碼時，來自I/O設備的相應中斷請求不會被CPU確認。這意味著CPU不會暫停當前任務來服務中斷。

- **控制**：中斷掩碼通常由一個寄存器控制，通常稱為中斷掩碼寄存器或中斷使能寄存器。通過設置或清除該寄存器中的位，系統可以啟用或禁用特定的中斷。

- **用例**：掩碼中斷通常用於代碼的關鍵部分，其中中斷可能會導致數據損壞或不一致。它還用於管理中斷優先級，確保更重要的中斷首先被處理。

- **恢復**：一旦執行了關鍵代碼部分，或系統準備好再次處理中斷，中斷掩碼可以調整以重新啟用中斷請求，使CPU能夠根據需要響應它們。

總結來說，中斷掩碼提供了一種控制CPU響應哪些中斷的方法，從而更好地管理系統資源和優先級。

---

算術邏輯單元（ALU）是中央處理單元（CPU）的基本組件，執行算術和邏輯操作。這裡是它的角色和功能概述：

- **算術操作**：ALU可以執行基本的算術操作，如加法、減法、乘法和除法。這些操作對數據處理和計算任務至關重要。

- **邏輯操作**：ALU還處理邏輯操作，包括AND、OR、NOT和XOR。這些操作用於位操作和CPU內的決策過程。

- **數據處理**：ALU處理來自CPU其他部分（如寄存器或存儲器）的數據，並根據控制單元的指示執行必要的計算。

- **指令執行**：當CPU從存儲器提取指令時，ALU負責執行該指令的算術或邏輯部分。這些操作的結果通常存儲回寄存器或存儲器。

- **CPU功能的重要組成部分**：ALU是CPU的數據路徑的一部分，並在執行程序時通過執行軟件指令所需的計算來發揮中心作用。

總結來說，ALU是執行數學和邏輯操作的CPU部分，使CPU能夠高效地處理數據和執行指令。

---

XOR（異或）操作是一種邏輯操作，比較兩個位並根據以下規則返回結果：

- **0 XOR 0 = 0**：如果兩個位都是0，結果是0。
- **0 XOR 1 = 1**：如果一個位是0，另一個位是1，結果是1。
- **1 XOR 0 = 1**：如果一個位是1，另一個位是0，結果是1。
- **1 XOR 1 = 0**：如果兩個位都是1，結果是0。

總結來說，XOR在位不同時返回1，在位相同時返回0。這種操作在各種應用中常用，包括：

- **錯誤檢測**：XOR用於奇偶檢查和錯誤檢測碼中，以識別數據傳輸中的錯誤。
- **加密**：在密碼學中，XOR用於簡單的加密和解密過程。
- **數據比較**：它可以用來比較兩組數據以識別差異。

XOR操作是數字邏輯和計算的基礎，提供了一種比較和操作位的方法。

---

串行傳輸是一種數據傳輸方法，其中數據一位一位地通過單一通信線或通道傳輸。這裡是串行傳輸的關鍵方面：

- **單線**：在串行傳輸中，數據位按順序一位接一位地傳輸，通過單一通信線。這與平行傳輸形成對比，平行傳輸同時通過多個線傳輸多個位。

- **逐位**：每個數據位按順序傳輸，這意味著傳輸一個字節（8位）需要八個連續的位傳輸。

- **簡單性和成本**：串行傳輸比平行傳輸更簡單和便宜，因為它需要更少的線和連接器。這使它適合長距離通信和需要減少物理連接數量的系統。

- **速度**：儘管串行傳輸通常比平行傳輸慢，但它可以通過先進的編碼和調製技術實現高速。

- **應用**：串行傳輸常用於各種通信系統，包括USB、以太網和許多無線通信協議。它還用於接口，如RS-232，用於將計算機連接到外圍設備。

總結來說，串行傳輸涉及一位一位地通過單線傳輸數據位，提供簡單性和成本效益，但速度不如平行傳輸。

---

你提供了一個常見I/O總線在計算機中的概述。讓我們澄清並擴展每個這些：

1. **PCI（外圍組件互連）總線**：
   - **描述**：PCI是一種平行總線標準，用於將外圍設備連接到計算機的CPU和存儲器。它被設計為與各種CPU兼容，這意味著它可以與各種CPU一起工作。
   - **特點**：支持多個外圍設備，以高時鐘頻率運行，並提供高數據傳輸速率。它在個人計算機中被廣泛用於連接組件，如圖形卡、聲音卡和網絡卡。
   - **後繼者**：PCI已經演變為更高性能和更先進功能的新標準，如PCI-X和PCI Express（PCIe）。

2. **USB（通用串行總線）**：
   - **描述**：USB是一種標準接口，用於將各種外圍設備連接到計算機。它簡化了連接和使用設備的過程，通過提供一個通用的即插即用接口。
   - **特點**：USB支持熱插拔，這意味著設備可以在不重新啟動計算機的情況下連接和斷開。它還為外圍設備提供電源，並支持適合許多設備的數據傳輸速率。
   - **版本**：USB有幾個版本，包括USB 1.1、USB 2.0、USB 3.0和USB4，每個版本都提供更高的數據傳輸速度和額外的功能。

3. **IEEE 1394（防火牆）**：
   - **描述**：由Apple開發並標準化為IEEE 1394，防火牆是一種高速串行總線，設計用於高帶寬應用。它在多媒體和存儲應用中常用。
   - **特點**：防火牆支持高數據傳輸速率，使其適合設備，如數字相機、外部硬盤和音頻/視頻設備。它還支持對等設備通信和等時數據傳輸，這對實時應用至關重要。
   - **應用**：儘管在專業音頻/視頻設備和某些消費電子產品中不如以前流行，防火牆曾經在專業音頻/視頻設備中非常受歡迎。

這些總線標準在現代計算和消費電子的發展中起著關鍵作用，使得連接各種設備的需求得以滿足，這些設備具有不同的性能要求。

---

在堆疊數據結構中，堆疊指針（SP）是一個寄存器，用於跟蹤堆疊的頂部。堆疊指針的初始值取決於架構和堆疊的具體實現。這裡有兩種常見的方法：

1. **完全下降堆疊**：在這種方法中，堆疊向下在存儲器中生長。堆疊指針初始化為分配給堆疊的最高存儲器地址。當項目被推入堆疊時，堆疊指針減量。

2. **空升堆疊**：在這種方法中，堆疊向上在存儲器中生長。堆疊指針初始化為分配給堆疊的最低存儲器地址。當項目被推入堆疊時，堆疊指針增量。

這兩種方法之間的選擇取決於系統的設計和慣例。在許多系統中，特別是那些使用下降堆疊的系統，堆疊指針的初始值設定為分配的堆疊空間的最高地址，並在數據被推入堆疊時減量。

---

在直接寻址模式中，操作數的地址直接在指令本身中指定。這意味著操作數的地址明確包含在指令代碼中。這裡是它的工作原理：

1. **指令格式**：指令包含一個操作碼（操作碼）和一個地址字段。地址字段直接指定操作數存儲在存儲器中的位置。

2. **執行**：當指令被執行時，CPU使用指令中指定的地址直接訪問存儲器位置。操作數從或存儲到該存儲器地址，而不需要任何進一步的地址計算。

3. **效率**：直接寻址簡單且高效，因為它涉及最少的地址計算。然而，它比其他寻址模式（如間接或索引寻址）更不靈活，因為地址在編寫指令時是固定的。

總結來說，在直接寻址中，操作數的地址明確包含在指令中，使CPU能夠直接從指定的存儲器位置訪問操作數。

---

要在單總線架構CPU中執行`ADD R1, R2, R3`指令，我們需要遵循一系列步驟，這些步驟涉及提取指令、解碼它並執行它。這裡是執行流程的詳細分解：

1. **指令提取**：
   - 程序計數器（PC）保存下一條要執行的指令的地址。
   - PC中的地址加載到存儲器地址寄存器（MAR）。
   - 存儲器讀取MAR指定地址處的指令並將其加載到存儲器數據寄存器（MDR）。
   - 指令然後從MDR轉移到指令寄存器（IR）。
   - PC增量以指向下一條指令。

2. **指令解碼**：
   - IR中的指令被解碼以確定操作（ADD）和操作數（R1、R2、R3）。

3. **操作數提取**：
   - R2和R3的地址放置在總線上以讀取它們的內容。
   - R2和R3的內容被提取並暫時存儲在緩衝區或直接用於下一步。

4. **執行**：
   - 算術邏輯單元（ALU）執行R2和R3的內容的加法。
   - 加法的結果暫時存儲在緩衝區或直接發送到下一階段。

5. **寫回**：
   - ALU的結果寫回寄存器R1。
   - R1的地址放置在總線上，結果存儲在R1中。

6. **完成**：
   - 指令執行完成，CPU準備好從PC中當前地址提取下一條指令。

這個序列概述了在單總線架構中執行`ADD`指令的基本流程，其中每個步驟涉及使用共享總線在CPU組件和存儲器之間傳輸數據。

---

在二進制算術中的“一位乘法”術語中，每個位（或位）的乘數被單獨考慮。這種方法類似於我們在十進制算術中進行乘法的方式，其中我們乘以一個數字的每個位數，並適當地移動結果。

這裡是為什麼它被稱為“一位乘法”：

1. **位操作**：在二進制乘法中，每個位的乘數被單獨處理。對於每個位為`1`的位，乘數被加到結果中，並適當地移位。對於每個位為`0`的位，乘數不被加，但位置仍然移位。

2. **移位和加法**：過程涉及將乘數向左移動一位，以便每次移動到下一個乘數位。這種移位對應於乘以2的幂，類似於在十進制乘法中移動位數對應於乘以10的幂。

3. **部分產品**：每一步產生一個部分產品，然後將它們相加以獲得最終結果。這與十進制乘法中的部分產品生成相似，其中部分產品是為每個乘數位生成的。

這個術語強調了方法的簡單性和基礎性，因為它將乘法過程分解為更小、更易管理的步驟，每個步驟涉及單個位。這種方法在數字系統和計算機算術中是基本的，因為操作在位級別上進行。

---

要使用四位有符號二進制數（原始碼）計算 \(4 \times 5\)，我們需要遵循這些步驟：

1. **將數字轉換為四位有符號二進制（原始碼）**：
   - \(4\)在四位有符號二進制中是\(0100\)。
   - \(5\)在四位有符號二進制中是\(0101\)。

2. **執行乘法**：
   - 將每個第二個數字的位乘以第一個數字的整個數字，並向左移動每次移動到下一個位。

這裡是逐步乘法過程：

```
    0100  (4 in binary)
  × 0101  (5 in binary)
  --------
    0100  (0100 × 1, no shift)
   0000   (0100 × 0, shift left by 1)
  0100    (0100 × 1, shift left by 2)
  --------
  0010100 (Sum of the partial products)
```

3. **求和部分產品**：
   - 將部分產品相加，我們得到\(0010100\)。

4. **將結果轉換回十進制**：
   - 二進制數\(0010100\)等於十進制的\(20\)。

因此，使用四位有符號二進制乘法計算\(4 \times 5\)的結果是\(20\)。

---

中斷是計算機系統中用於處理需要立即注意的事件的機制。它們允許CPU通過暫停當前任務並執行特定的中斷處理程序或中斷服務例程（ISR）來響應外部或內部事件。這裡是中斷類型的分解：

1. **外部中斷（硬件中斷）**：這些由硬件設備觸發，以表示它們需要注意。例如，鍵盤中斷在按下鍵時發生，網絡中斷在接收數據時發生。外部中斷是非同步的，這意味著它們可以在任何時候發生，而不考慮CPU正在做什麼。

2. **內部中斷（例外）**：這些由CPU本身在執行指令時生成，以響應某些條件。例如：
   - **除以零**：在尝試除以零的除法操作時觸發。
   - **非法指令**：在CPU遇到無法執行的指令時觸發。
   - **溢出**：在算術操作超出數據類型的最大大小時觸發。

3. **軟件中斷**：這些由軟件使用特定指令故意觸發。它們通常用於調用系統調用或在不同模式之間切換（例如，從用戶模式切換到內核模式）。軟件中斷是同步的，這意味著它們是執行特定指令的直接結果。

每種中斷類型在管理系統資源和確保CPU能夠高效地響應緊急或例外條件方面都起著特定的作用。

---

在計算機系統中，特別是在討論總線架構時，術語“主設備”和“從設備”通常用來描述設備在總線通信中的角色。這裡是這些術語的分解：

1. **主設備**：這是控制總線的設備。主設備通過發送命令和地址來啟動數據傳輸，並管理通信過程。它可以從其他設備讀取或寫入數據，這些設備連接到總線。

2. **從設備**：這是響應主設備發出的命令的設備。從設備被主設備訪問，並可以將數據發送到或從主設備接收數據。它不會啟動通信，而是響應主設備的請求。

這些角色對於在計算機系統中協調數據傳輸至關重要，例如CPU、存儲器和外圍設備。

---

在計算機中，寄存器是CPU內部的小型、快速存儲位置，用於在處理過程中暫時存儲數據。有幾種類型的寄存器，每種都有特定的用途：

1. **通用寄存器（GPRs）**：這些用於各種數據操作任務，如算術操作、邏輯操作和數據傳輸。例如，x86架構中的AX、BX、CX和DX寄存器。

2. **特殊用途寄存器**：這些有特定功能，並不適合所有類型的數據操作。例如：
   - **指令寄存器（IR）**：保存當前正在執行的指令。
   - **程序計數器（PC）**：包含下一條要執行的指令的地址。
   - **堆疊指針（SP）**：指向堆疊在存儲器中的頂部。
   - **基地址和索引寄存器**：用於存儲器寻址。

3. **段寄存器**：在某些架構（如x86）中，用於保存存儲器段的基地址。例如，代碼段（CS）、數據段（DS）和堆疊段（SS）寄存器。

4. **狀態寄存器或標誌寄存器**：保存指示上次操作結果的條件碼或標誌，例如零標誌、進位標誌、符號標誌和溢出標誌。

5. **控制寄存器**：用於控制CPU操作和模式。例如，x86架構中的控制寄存器管理分頁、保護和其他系統級功能。

6. **浮點寄存器**：用於浮點算術操作的CPU支持浮點硬件。

7. **常量寄存器**：某些架構具有保存常量值（如零或一）的寄存器，以優化某些操作。

這些寄存器共同工作，促進指令執行、數據流管理和CPU操作的控制。

---

機器指令，也稱為機器代碼指令，是CPU（中央處理單元）可以直接執行的低級命令。每條指令通常包含幾個關鍵組件：

1. **操作碼（Opcode）**：這指定要執行的操作，例如加法、減法、加載、存儲等。操作碼告訴CPU要採取什麼行動。

2. **操作數**：這些是指令將操作的數據項或值。操作數可以是立即值（常數）、寄存器或存儲器地址。

3. **寻址模式**：這決定如何訪問操作數。常見的寻址模式包括立即寻址、直接寻址、間接寻址和寄存器寻址。

4. **指令格式**：這定義了指令的結構，包括操作碼和操作數在指令中的大小和位置。

5. **條件碼**：某些指令可能會影響或受條件碼或標誌影響，這些標誌是特殊用途寄存器，保存操作結果的狀態信息（例如，零標誌、進位標誌）。

這些組件共同定義了一個精確的動作，CPU將執行該動作，例如移動數據、執行算術操作或控制程序流程。

---

是的，你描述的是**寄存器直接寻址**，這是計算機架構中的另一種寻址模式。這裡是它的解釋：

### 寄存器直接寻址（寄存器直接寻址）：
- **速度**：非常快
- **解釋**：在寄存器直接寻址中，指令指定一個包含操作數的寄存器。操作數直接從寄存器訪問，而不從存儲器訪問。這種模式非常快，因為訪問寄存器比訪問存儲器快得多。寄存器是CPU的一部分，因此不需要存儲器訪問周期。

- **例子**：
  ```assembly
  ADD A, R1
  ```
- **解釋**：在這個例子中，指令將寄存器`R1`中的值加到寄存器`A`中。操作數直接可用於寄存器`R1`，因此CPU可以快速執行操作而不需要訪問存儲器。

寄存器直接寻址效率高，因為它利用了寄存器的速度，使其成為最快的寻址模式之一。它在操作數頻繁訪問或修改的操作中常用，例如在循環或算術操作中。

---

好的！讓我們通過每種寻址模式的例子來說明它們的工作原理：

1. **立即寻址（立即寻址）**：
   - **例子**：
     ```assembly
     MOV A, #5
     ```
   - **解釋**：在這個例子中，值`5`直接包含在指令中。CPU將值`5`移動到寄存器`A`，而不需要訪問存儲器。這是立即寻址，因為操作數（`5`）立即可用於指令。

2. **直接寻址（直接寻址）**：
   - **例子**：
     ```assembly
     MOV A, [1000]
     ```
   - **解釋**：在這個例子中，指令告訴CPU將存儲器地址`1000`處的值移動到寄存器`A`。操作數位於特定的存儲器地址，因此CPU需要訪問存儲器以檢索它。這是直接寻址，因為操作數的地址直接指定在指令中。

3. **間接寻址（間接寻址）**：
   - **例子**：
     ```assembly
     MOV A, [B]
     ```
   - **解釋**：在這個例子中，寄存器`B`包含一個地址（例如`2000`）。CPU首先從寄存器`B`檢索地址，然後訪問存儲器地址`2000`以獲取實際操作數值，然後將該值移動到寄存器`A`。這是間接寻址，因為指令指向一個包含操作數地址的位置，增加了一個間接層。

這些例子說明了每種寻址模式如何訪問操作數，從立即寻址的最直接和最快，到間接寻址的最間接和最慢。

---

在計算機架構中，寻址模式決定了指令的操作數如何訪問。這裡是從最快到最慢的三種寻址模式的解釋：

1. **立即寻址（立即寻址）**：
   - **速度**：最快
   - **解釋**：在立即寻址中，操作數是指令的一部分。這意味著數據立即可用，不需要進一步的存儲器訪問來檢索操作數。這使它成為最快的模式，因為CPU可以立即使用數據而不需要任何進一步的查找。

2. **直接寻址（直接寻址）**：
   - **速度**：快
   - **解釋**：在直接寻址中，指令包含操作數的存儲器地址。CPU直接訪問該地址以檢索操作數。這種模式比立即寻址慢，因為它需要一個存儲器訪問周期來檢索操作數。

3. **間接寻址（間接寻址）**：
   - **速度**：最慢
   - **解釋**：在間接寻址中，指令包含一個地址，該地址指向另一個地址，該地址包含實際操作數。這可能涉及多個存儲器訪問：首先獲取操作數的地址，然後獲取操作數本身。這個額外的間接層使它成為最慢的模式。

總結來說，立即寻址是最快的，因為操作數直接可用；直接寻址需要一個存儲器訪問來檢索操作數；間接寻址需要多個存儲器訪問來檢索操作數，因此是最慢的。
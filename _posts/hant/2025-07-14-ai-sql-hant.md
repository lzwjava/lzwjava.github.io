---
audio: false
generated: false
lang: hant
layout: post
title: 使用AI建構SQL查詢
translated: true
---

**資料庫架構 (PostgreSQL):**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(10),
    phone_number VARCHAR(20),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    zip_code VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    role VARCHAR(50),
    profile_picture_url VARCHAR(255),
    bio TEXT,
    failed_login_attempts INTEGER DEFAULT 0,
    account_balance NUMERIC(10, 2) DEFAULT 0.00
);
```

---

以上是PostgreSQL資料庫，以下是表格定義。以下是自然語言查詢指示。

我要獲取一些名字是Andy的用戶，創建時間在上個月的日期附近，2025年時年齡為20歲，且最近一週有登入記錄，請提供查詢這些用戶的SQL。

---

**生成的SQL查詢:**
```sql
SELECT *
FROM users
WHERE first_name ILIKE 'andy'
  AND CAST(created_at AS DATE) BETWEEN
      (CURRENT_DATE - INTERVAL '1 MONTH' - INTERVAL '1 DAY')
      AND
      (CURRENT_DATE - INTERVAL '1 MONTH' + INTERVAL '1 DAY')
  AND EXTRACT(YEAR FROM AGE(date_of_birth)) = 20
  AND last_login >= CURRENT_TIMESTAMP - INTERVAL '7 DAYS';
```
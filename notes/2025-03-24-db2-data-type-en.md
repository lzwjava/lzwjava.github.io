---
title: IBM Db2 Data Types
lang: en
layout: post
audio: false
translated: false
generated: true
---

Db2 supports a wide range of data types to accommodate various data storage needs. Here's a comprehensive overview of Db2 data types by category:

## Numeric Data Types

### Integer Types
- **SMALLINT**: 16-bit integer (-32,768 to 32,767)
- **INTEGER** or **INT**: 32-bit integer (-2,147,483,648 to 2,147,483,647)
- **BIGINT**: 64-bit integer (approximately -9.2E18 to 9.2E18)

### Decimal Types
- **DECIMAL(p,s)** or **DEC(p,s)** or **NUMERIC(p,s)**: Exact decimal values where 'p' is precision (total digits) and 's' is scale (decimal places)
- **DECFLOAT**: Decimal floating-point that follows the IEEE 754r standard, available in 16-digit or 34-digit precision

### Floating-Point Types
- **REAL** or **FLOAT(1-24)**: 32-bit floating-point number
- **DOUBLE** or **DOUBLE PRECISION** or **FLOAT(25-53)**: 64-bit floating-point number

## Character Data Types

### Fixed-Length
- **CHAR(n)** or **CHARACTER(n)**: Fixed-length character string (1-255 bytes)

### Variable-Length
- **VARCHAR(n)** or **CHARACTER VARYING(n)**: Variable-length character string (1-32,672 bytes)
- **CLOB** or **CHARACTER LARGE OBJECT**: Large character objects (up to 2GB)

### Graphic Types (for DBCS characters)
- **GRAPHIC(n)**: Fixed-length double-byte string
- **VARGRAPHIC(n)**: Variable-length double-byte string
- **DBCLOB**: Double-byte character large object

## Binary Data Types
- **BINARY(n)**: Fixed-length binary data
- **VARBINARY(n)** or **BINARY VARYING(n)**: Variable-length binary data
- **BLOB** or **BINARY LARGE OBJECT**: Binary large objects (up to 2GB)

## Date and Time Data Types
- **DATE**: Calendar date (YYYY-MM-DD)
- **TIME**: Time of day (HH:MM:SS)
- **TIMESTAMP**: Date and time (YYYY-MM-DD-HH.MM.SS.nnnnnn)
- **TIMESTAMP WITH TIME ZONE**: Timestamp that includes time zone information

## Boolean Type
- **BOOLEAN**: TRUE, FALSE, or NULL values

## XML Data Type
- **XML**: Stores XML documents in their hierarchical form

## Row Types
- **ROW**: Structured type comprising a sequence of named fields with associated data types

## User-Defined Types
- **Distinct Types**: Based on built-in data types but incompatible with their source types
- **Structured Types**: User-defined types with attributes and methods

## Special Types
- **ROWID**: Row identifier, a value that uniquely identifies a row
- **DATALINK**: References to external files
- **ARRAY**: Ordered collection of elements of the same type

Each data type in Db2 has specific storage requirements, performance characteristics, and usage scenarios. The choice of data type affects database performance, storage efficiency, and data integrity.
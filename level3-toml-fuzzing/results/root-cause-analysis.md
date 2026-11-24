# Level 3 – Root Cause Analysis

## 1. BUG-001 and BUG-002: Control Character Handling

**Component:** TOML Encoder

The encoder does not correctly handle dictionary keys containing control characters during string serialization.

- **BUG-001 – Key Corruption:** A control character in a dictionary key is incorrectly converted into different text during serialization. As a result, the original key is not preserved after deserialization.
- **BUG-002 – Encoder Crash:** Certain control characters cause the encoder to raise an `IndexError` instead of producing valid TOML output or a controlled validation error.

**Source location:** `toml/encoder.py`, around line 113, within the `_dump_str()` function.

**Root cause:** The string-encoding logic splits strings around hexadecimal escape sequences and assumes that the resulting list contains the required elements. Certain control-character combinations violate this assumption, resulting in incorrect serialization or an indexing error.

## 2. BUG-003 and BUG-005: Incomplete Array Acceptance

**Component:** TOML Decoder

The `load_array()` function processes array contents using `a[1:-1]`, assuming that the input contains both opening and closing square brackets.

However, malformed arrays without a closing bracket are accepted instead of being rejected.

- **BUG-003:** The incomplete array `name = [1, 2,` is accepted.
- **BUG-005:** The incomplete array `array = [` is interpreted as an empty array.

**Source location:** `toml/decoder.py`, lines 944–951 and 1009–1033, within the `load_array()` function.

**Root cause:** The decoder does not adequately validate the presence of the closing bracket before processing the array contents.

**Assessment:** Both bugs appear to share the same underlying defect in array parsing, although they produce different incorrect results.

## 3. BUG-004: Incomplete Inline Table Acceptance

**Component:** TOML Decoder

The `load_inline_object()` function processes inline tables using `line[1:-1]`, assuming that the input contains both opening and closing curly braces.

An incomplete inline table such as `key = {` is incorrectly interpreted as an empty table instead of being rejected.

**Source location:** `toml/decoder.py`, lines 654–665, within the `load_inline_object()` function.

**Root cause:** The decoder does not adequately validate the closing brace before processing inline-table contents.

## 4. Reference Parser and Differential Comparison

Python's built-in `tomllib` module was used as the reference parser for differential testing.

The malformed array and inline-table inputs identified in BUG-003, BUG-004 and BUG-005 were rejected by `tomllib` but accepted by `toml==0.10.2`.

This difference demonstrates that the third-party parser accepts certain malformed TOML documents that the reference parser rejects.

## 5. Proposed Fixes

Two areas were selected for proposed fixes:

1. **Encoder string handling:** Introduced a separate string-encoding function that escapes control characters and preserves the original string values.
2. **Decoder array validation:** Introduced validation to check for opening and closing square brackets before processing array contents.

The proposed fixes were tested independently using regression tests.

**Validation results:**
- Encoder fix: 3 tests passed.
- Decoder fix: 3 tests passed.

These fixes are isolated proposals and do not modify the installed `toml==0.10.2` package.
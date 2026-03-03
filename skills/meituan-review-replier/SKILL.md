---
name: meituan-review-replier
description: Automated Meituan/Dianping review response system. Use when replying to customer reviews on Chinese platforms (ecom.meituan.com). Supports warm style for positive reviews and sincere problem-solving for negative reviews.
license: Complete terms in LICENSE.txt
---

# Meituan Review Replier

Automated review response system for Meituan business platform.

## Quick Start

Navigate to review management:
```
https://ecom.meituan.com/emis/evaluation/poi
```

Filter unreplied reviews and respond with appropriate style based on rating.

## Response Styles

For detailed style guides and templates, see [references/styles.md](references/styles.md).

**Positive Reviews (4-5 stars)** - Warm, friendly tone
**Negative Reviews (0.5-3.5 stars)** - Sincere, solution-oriented

## Workflow

1. **Open Review Page** → Navigate to management URL
2. **Select Platform** → Choose "美团评价" or "点评评价"
3. **Filter Unreplied** → Click "未回复"
4. **Set Time Filter** → Start with "近7天"
5. **Check Results** → If 0 reviews, ask user before switching to "近30天"
6. **Check Multi-Store** → Click store selector, check each store
7. **For Each Review** → Select style, click reply, fill content, submit
8. **Summary Report** → Report results in table format

## Time Filter Logic

```
近7天 → 0 results? → Ask user → 近30天 (if confirmed)
                      → Skip if declined
```

## Key URLs

| Purpose | URL |
|---------|-----|
| Review Management | https://ecom.meituan.com/emis/evaluation/poi |
| Login | https://ecom.meituan.com/meishi |

## Notes

- Always check "近7天" first before "近30天"
- Match response style to review rating
- Wait 2-3 seconds after sending to verify
- Report summary in table format for multi-store

## Resources

- [references/styles.md](references/styles.md) - Complete response style templates and examples
- [references/workflow.md](references/workflow.md) - Detailed workflow with screenshots

---
name: meituan-review-replier
description: Automated Meituan/Dianping review response system. Use when user needs to reply to customer reviews on Meituan business platform (ecom.meituan.com). Automatically navigates to review management page, identifies unreplied reviews, generates context-appropriate responses based on review rating, and submits replies. Supports "warm sister" style for positive reviews and "sincere problem-solving" style for negative reviews.
---

# Meituan Review Replier

Automated review response system for Meituan business platform.

## Quick Start

```bash
# Navigate to review management page
Navigate to: https://ecom.meituan.com/meishi/?cate=6103#https://ecom.meituan.com/emis/evaluation/poi

# Identify unreplied reviews
Check for "未回复" filter or look for reviews with "回复" button visible
```

## Response Styles

### For Positive Reviews (4-5 stars) - "Warm Sister" Style

Tone: Friendly, warm, enthusiastic, like a caring sister

**Template:**
```
{Warm opening acknowledging their praise}

{Respond to specific points they mentioned (food quality, taste, atmosphere)}

{Express gratitude and invite them back with small personal touch}
```

**Example:**
```
哇！看到你这么喜欢我们家的[菜名]，姐姐心里美滋滋的😊~

你说得对！我们家就是坚持现炒现做，这样才能吃出那种锅气的香味。期待你常来光顾，姐姐下次给你多加点小菜😉
```

### For Negative/Mixed Reviews (0.5-3.5 stars) - "Sincere Problem-Solving" Style

Tone: Sincere, apologetic, solution-oriented, taking responsibility

**Template:**
```
{Acknowledge the problem sincerely - this hurts us too}

{Show we understand their frustration and value their expectations}

{Offer concrete solution - invite them back for free experience}

{End with commitment to improvement}
```

**Example:**
```
非常扎心，但也非常感谢您的直言不讳。

每一个差评背后，都是一位对我们抱有期待的客人。今天的用餐体验离我们的标准相差甚远。

千言万语不如实际行动，希望能有个机会，邀请你再次到店免费体验一次，让我们把坏事变好事，用真正的服务和品质重新赢回您的认可和好评。
```

## Workflow

1. **Open Review Page**: Navigate to Meituan business review management
2. **Select Platform**: Choose "美团评价" or "点评评价" tab
3. **Filter Unreplied**: Click "未回复" button to show pending reviews
4. **Set Time Filter to "近7天"**: Check last 7 days for unreplied reviews
5. **Check Results**:
   - If 0 reviews → Ask user: "近7天无未回复评价，需要切换到近30天查看吗？"
   - If user agrees → Click "近30天" button
6. **Check Multi-Store**:
   - Click store selector dropdown to see all stores
   - For each store: Select store → Check unreplied reviews → Reply if needed
   - Move to next store until all stores checked
7. **For Each Review**:
   - Check star rating
   - Select appropriate response style (warm sister for 4-5 stars, sincere for 0.5-3.5 stars)
   - Click "回复" button
   - Fill in response content
   - Click "发送" to submit
8. **Summary Report**: Report results for all stores in table format

## Time Filter Workflow

**Step 1: Always check "近7天" first**
- Click "未回复" filter
- Click "近7天" time filter
- Report result count

**Step 2: If 0 results, ask user before proceeding**
- "近7天无未回复评价，需要切换到近30天查看吗？"
- Only proceed to "近30天" after user confirmation

**Step 3: Check all stores if multi-store account**
- Click store name dropdown
- Iterate through all stores
- Report summary for each store

## Key URLs

- Review Management: https://ecom.meituan.com/meishi/?cate=6103#https://ecom.meituan.com/emis/evaluation/poi
- Login: https://ecom.meituan.com/meishi

## Notes

- **Progressive time filtering**: Always check "近7天" first, ask user before checking "近30天"
- **Multi-store support**: Click store selector to see all stores, check each store individually
- **Always match response style to review rating**
- **Keep responses warm and personal for positive reviews**
- **Be sincere and solution-focused for negative reviews**
- **Wait 2-3 seconds after clicking "发送" before refreshing**
- **Verify reply button disappeared to confirm success**
- **Report summary in table format** when checking multiple stores

## Example Summary Report

```
| 门店 | 近7天未回复 | 近30天未回复 |
|------|------------|-------------|
| 世纪莲地铁店 | 0 条 | 0 条 |
| 金铂中心店 | - | 0 条 |
| 万民金海店 | - | 0 条 |
```

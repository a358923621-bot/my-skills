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
3. **Set Time Filter** (Optional): Click time range buttons to filter reviews
   - **全部** - All time
   - **近7天** - Last 7 days (recommended for regular replies)
   - **近30天** - Last 30 days
   - Or set custom date range using date picker
4. **Filter Unreplied**: Click "未回复" button to show pending reviews
5. **For Each Review**:
   - Check star rating
   - Select appropriate response style
   - Click "回复" button
   - Fill in response content
   - Click "发送" to submit
6. **Verify**: Refresh page to confirm reply was submitted

## Time Filter Guidelines

- **Daily routine**: Use "近7天" to catch recent reviews
- **Weekly catch-up**: Use "近30天" for comprehensive review
- **Custom range**: Use date picker for specific period (e.g., "2026/01/29 - 2026/02/04")

## Key URLs

- Review Management: https://ecom.meituan.com/meishi/?cate=6103#https://ecom.meituan.com/emis/evaluation/poi
- Login: https://ecom.meituan.com/meishi

## Notes

- Always match response style to review rating
- Keep responses warm and personal for positive reviews
- Be sincere and solution-focused for negative reviews
- Wait 2-3 seconds after clicking "发送" before refreshing
- Verify reply button disappeared to confirm success

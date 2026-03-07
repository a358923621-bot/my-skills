# Detailed Workflow Guide

Complete step-by-step guide for responding to Meituan reviews.

## Initial Setup

### Login to Meituan Business Platform

URL: https://ecom.meituan.com/meishi

Use your business account credentials to log in.

---

## Main Workflow

### Step 1: Navigate to Review Management Page

**URL**: https://ecom.meituan.com/emis/evaluation/poi

**Expected View**: Review management dashboard with filter options

---

### Step 2: Select Platform

Two options available:
- **美团评价** - Meituan reviews
- **点评评价** - Dianping reviews

**Action**: Click appropriate tab based on which platform you want to respond to.

---

### Step 3: Filter Unreplied Reviews

**Action**: Click "未回复" button

**Result**: Shows only reviews that haven't been responded to yet.

---

### Step 4: Set Time Filter - Progressive Approach

**IMPORTANT**: Always check "近7天" first, only proceed to "近30天" after user confirmation.

**Step 4a**: Click "近7天" time filter
**Step 4b**: Count and report results

**If 0 results**:
```
Ask user: "近7天无未回复评价，需要切换到近30天查看吗？"
```

**If user confirms**: Click "近30天" button
**If user declines**: End workflow for this store/platform

---

### Step 5: Check Multi-Store

Many accounts manage multiple stores.

**Step 5a**: Click store name dropdown selector
**Step 5b**: List of all stores appears

**For each store**:
1. Select store from dropdown
2. Check unreplied reviews count
3. Respond to reviews (see Step 6)
4. Move to next store

**Continue until all stores are processed.**

---

### Step 6: Respond to Each Review

For each unreplied review:

**6a. Check star rating**
- 4-5 stars → Use Warm Sister style
- 0.5-3.5 stars → Use Sincere Problem-Solving style

**6b. Click "回复" button**

**6c. Generate response**
- Reference appropriate style guide
- Customize based on review content
- Address specific points mentioned

**6d. Fill in response content**

**6e. Click "发送" to submit**

**6f. Wait 2-3 seconds**
- Allow submission to complete
- Verify reply button disappeared (confirms success)

**6g. Repeat for next review**

---

### Step 7: Summary Report

After processing all stores, generate summary report:

```
| 门店 | 近7天未回复 | 近30天未回复 |
|------|------------|-------------|
| [Store Name 1] | [count] 条 | [count] 条 |
| [Store Name 2] | [count] 条 | [count] 条 |
| [Store Name 3] | [count] 条 | [count] 条 |
```

**Report format**:
- Use table format
- Show counts for both time periods
- Include "- " if no data for that period
- Highlight stores with pending reviews

---

## Time Filter Decision Tree

```
START
  ↓
近7天 → Count reviews
  ↓
  ├─→ Reviews found? → YES → Process reviews
  │                          ↓
  │                       近30天? → Ask user
  │                          ↓
  │                       ├─→ YES → Check 近30天
  │                       └─→ NO → END
  │
  └─→ 0 reviews → Ask user: "切换到近30天?"
       ↓
       ├─→ YES → 近30天 → Process
       └─→ NO → END
```

---

## Multi-Store Workflow

```
START
  ↓
Click store dropdown → List all stores
  ↓
For each store:
  ├─→ Select store
  ├─→ Check 近7天 unreplied
  ├─→ If 0, ask about 近30天
  ├─→ Process all reviews
  ├─→ Verify each submission
  └─→ Move to next store
  ↓
All stores done → Generate summary table
```

---

## Verification Checklist

After responding to each review, verify:

- [ ] Reply button disappeared (submission successful)
- [ ] Response content matches style guidelines
- [ ] Specific points in review were addressed
- [ ] Waited 2-3 seconds before refreshing
- [ ] Next review loaded correctly

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Reply button still visible | Wait 3-5 seconds, check if submission failed |
| Can't find "未回复" filter | Refresh page, check if you have correct permissions |
| Store dropdown empty | Account may only manage one store |
| Submission fails | Check network connection, log in again |

---

## Key URLs Reference

| Purpose | URL |
|---------|-----|
| Login | https://ecom.meituan.com/meishi |
| Review Management | https://ecom.meituan.com/emis/evaluation/poi |

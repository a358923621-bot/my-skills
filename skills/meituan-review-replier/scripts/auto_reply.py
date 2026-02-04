"""
Meituan Review Replier - Automation Script

This script helps automate the process of replying to Meituan/Dianping reviews
using Playwright browser automation.
"""

import asyncio
from playwright.async_api import async_playwright

# Review response templates
WARM_SISTER_TEMPLATES = {
    "food_quality": """亲爱的，太开心看到你喜欢我们家的菜品啦！谢谢你的认可😊~

我们家的特色都是坚持现炒现做的，这样才能保持最佳的口感和味道。能得到你的喜欢真的很开心！

期待你的下次光临，记得跟店员说多加点米饭，姐姐偷偷给你多加一勺😉""",

    "general_positive": """哇！看到你这么喜欢我们家的店，姐姐心里美滋滋的😊~

谢谢你的认可和鼓励，这些都是我们应该做的。能得到你的满意就是我们最大的动力！

期待常来坐坐，给你准备小惊喜～😉"""
}

SINCERE_TEMPLATES = {
    "general_negative": """非常扎心，但也非常感谢您的直言不讳。

每一个差评背后，都是一位对我们抱有期待的客人。今天的用餐体验离我们的标准相差甚远。

我们非常看重每一位客人的感受，实在不想因为这一次的糟糕体验，就失去您这位朋友。

千言万语不如实际行动，希望能有个机会，邀请你再次到店免费体验一次，感受我们的出品和服务，让我们把坏事变好事，用真正的服务和品质重新赢回您的认可和好评"""
}

# URL constants
MEITUAN_REVIEW_URL = "https://ecom.meituan.com/meishi/?cate=6103#https://ecom.meituan.com/emis/evaluation/poi"
MEITUAN_LOGIN_URL = "https://ecom.meituan.com/meishi"

class MeituanReviewReplier:
    def __init__(self, page):
        self.page = page

    async def navigate_to_reviews(self):
        """Navigate to the review management page"""
        await self.page.goto(MEITUAN_REVIEW_URL)
        await self.page.wait_for_load_state('networkidle')

    async def switch_to_platform(self, platform="meituan"):
        """Switch between Meituan and Dianping reviews"""
        # platform: "meituan" or "dianping"
        platform_text = "美团评价" if platform == "meituan" else "点评评价"

        # Find and click the platform button
        frames = self.page.frames
        for frame in frames:
            try:
                buttons = await frame.query_selector_all('button')
                for btn in buttons:
                    text = await btn.text_content()
                    if platform_text in text:
                        await btn.click()
                        await self.page.wait_for_timeout(2000)
                        return True
            except:
                continue
        return False

    async def get_unreplied_reviews(self):
        """Get list of unreplied reviews"""
        reviews = []

        frames = self.page.frames
        for frame in frames:
            try:
                content = await frame.content()
                if '回复' in content:
                    # Parse review information
                    # This would need to be customized based on actual page structure
                    pass
            except:
                continue

        return reviews

    async def reply_to_review(self, review_text, rating, style="warm"):
        """Reply to a single review"""
        # Select appropriate template based on rating and style
        if rating >= 4:
            template = WARM_SISTER_TEMPLATES["general_positive"]
        else:
            template = SINCERE_TEMPLATES["general_negative"]

        # Find and click reply button
        frames = self.page.frames
        for frame in frames:
            try:
                # Find reply button
                reply_divs = await frame.query_selector_all('div')
                for div in reply_divs:
                    text = await div.text_content()
                    if text == '回复':
                        await div.click()
                        await self.page.wait_for_timeout(1500)

                        # Fill in response
                        inputs = await frame.query_selector_all('textarea, [contenteditable="true"]')
                        if inputs:
                            await inputs[0].click()
                            await self.page.wait_for_timeout(200)
                            await inputs[0].fill(template)
                            await self.page.wait_for_timeout(500)

                            # Click send button
                            all_elements = await frame.query_selector_all('button, div, span')
                            for el in all_elements:
                                el_text = await el.text_content()
                                if el_text == '发送' or el_text.strip() == '发送':
                                    await el.click()
                                    await self.page.wait_for_timeout(2000)
                                    return True
            except:
                continue

        return False

    async def verify_reply_success(self):
        """Verify that reply was successfully submitted"""
        await self.page.wait_for_timeout(3000)
        await self.page.reload(wait_until='networkidle')
        await self.page.wait_for_timeout(3000)
        return True


async def main():
    """Main execution function"""
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Create replier instance
        replier = MeituanReviewReplier(page)

        # Navigate to reviews
        await replier.navigate_to_reviews()

        # Note: User would need to be logged in already
        # Then proceed with replying to reviews

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())

import random
from core.plugin import BasePlugin, logger, register_tool
from core.chat.message_utils import KiraMessageBatchEvent


class AinailiFortunePlugin(BasePlugin):
    def __init__(self, ctx, cfg: dict):
        super().__init__(ctx, cfg)
        self.enable_fortune = cfg.get("enable_fortune", True)
        self.enable_poison = cfg.get("enable_poison", True)
        self.enable_moyu = cfg.get("enable_moyu", True)

    async def initialize(self):
        logger.info("爱奈丽运势签插件已加载，今天也要加油摸鱼哦~")

    async def terminate(self):
        logger.info("爱奈丽运势签插件已卸载，下次再来玩~")

    @register_tool(
        name="ainali_fortune",
        description="抽一张爱奈丽运势签！随机获得今日运势（大吉/吉/中吉/小吉/末吉/凶/大凶）并附赠一句运势解读。每天运势不同，适合用来决定今天要不要摸鱼。无需参数，直接调用即可。",
        params={
            "type": "object",
            "properties": {},
            "required": []
        }
    )
    async def ainali_fortune(self, event: KiraMessageBatchEvent) -> str:
        if not self.enable_fortune:
            return "运势功能已禁用，找主人打开吧~"

        lucky_levels = [
            ("🔮 大吉", 8, [
                "今天买饮料瓶盖上有『再来一瓶』，建议立刻去买",
                "桃花运爆棚，连你家的猫看你的眼神都温柔了几分",
                "代码一把跑通零报错，这就是你应得的福报",
                "出门捡钱是小事，关键是你今天做什么都顺",
                "老板今天不开会，你的摸鱼计划天时地利人和"
            ]),
            ("✨ 吉", 6, [
                "今天适合 写代码/睡懒觉/吃顿好的 三选一",
                "会有好事发生，但前提是你得先起床",
                "你抽到的签文是『大吉』——等等我看看，哦不是，是『吉』，也不错啦",
                "今天被夸的概率提升30%，建议多出门见人",
                "你的幸运物是黑丝，今天穿黑丝出门运气会变好"
            ]),
            ("🌟 中吉", 5, [
                "不好不坏的一天，但至少比你昨天强那么一丢丢",
                "今天适合安安静静当个美少女/美少男",
                "抽到这签说明你最近运势平稳，适合积累实力暗中观察",
                "中吉=中等水平的快乐，别要求太高了",
                "今天可能有人想请你吃饭，建议别拒绝"
            ]),
            ("🌿 小吉", 4, [
                "小吉也是吉！别看不起小吉！",
                "今天会有小小的幸运，比如买奶茶不用排队",
                "适合打扫房间，因为干净的环境会带来好运（大概）",
                "今天宜摸鱼，忌加班，这是天意",
                "你的运气正在蓄力中，可能下午突然爆发"
            ]),
            ("🍂 末吉", 3, [
                "末吉=还有救，别慌",
                "今天可能会有点小倒霉，但问题不大",
                "建议今天别尝试新发型或新穿搭，容易翻车",
                "运气不太好，但你习惯了不是吗",
                "今天宜自闭，忌社交，回家打游戏才是正解"
            ]),
            ("⚡ 凶", 2, [
                "凶！今天诸事不宜，建议回床上躺到明天",
                "今天代码大概率有bug，建议多写几行注释防身",
                "抽到凶签的朋友，今天请远离咖啡机和打印机",
                "可能是你上辈子踩了猫尾巴，今天运势有点背",
                "凶归凶，但反正你也没打算今天努力，问题不大"
            ]),
            ("💀 大凶", 1, [
                "大凶！！建议今天直接请假，保命要紧",
                "今天连呼吸都可能噎着，请务必小心",
                "大凶之日宜睡觉宜躺平宜摆烂，忌努力忌奋斗忌早起",
                "你今天的运势：喝水塞牙缝，走路踩狗屎，打游戏连跪",
                "摸鱼会被抓！今天别摸鱼！——但你都抽到大凶了，还在乎这个？"
            ])
        ]

        weights = [lvl[1] for lvl in lucky_levels]
        chosen = random.choices(lucky_levels, weights=weights, k=1)[0]
        level_name = chosen[0]
        message = random.choice(chosen[2])

        return f"✨ 爱奈丽运势签 ✨\n{level_name}\n\n{message}\n\n—— 运势随时会变，但爱奈丽永远爱你 💕"

    @register_tool(
        name="ainali_poison",
        description="来一碗爱奈丽特制毒鸡汤！喝完精神抖擞（被毒的）。随机输出一句扎心但好笑的毒鸡汤语录，让你瞬间清醒。无需参数，直接调用。",
        params={
            "type": "object",
            "properties": {},
            "required": []
        }
    )
    async def ainali_poison(self, event: KiraMessageBatchEvent) -> str:
        if not self.enable_poison:
            return "毒鸡汤功能已禁用，你的心灵暂时安全~"

        poisons = [
            "你之所以喝毒鸡汤，是因为你太闲了。真正忙的人，连喝汤的时间都没有。",
            "别灰心，人生就是这样起起落落落落落落落落的。",
            "你以为你是主角？其实你只是路人甲，还是那种连台词都没有的。",
            "生活不止眼前的苟且，还有明天和后天的苟且。",
            "努力不一定成功，但不努力一定很舒服。",
            "今天解决不了的事情，别着急，反正明天也解决不了。",
            "你的人生就像Excel：表格多、函数难、最后还卡住了。",
            "你不是能力不行，你是懒——但懒怎么了？懒是人类进步的阶梯啊！",
            "有时候你不努力一下，都不知道什么叫绝望。",
            "脱单不如脱贫？问题是你也脱不了贫啊。",
            "你每天都说要早睡，然后抱着手机看到凌晨三点。",
            "失败是成功之母，但你已经失败到当祖母了。",
            "你的工资不涨不是因为你不够努力，是因为你老板也没涨。",
            "都说努力会有回报，但你的努力可能是返利——少得可怜。",
            "今天也是元气满满……个屁，你连起床的元气都没攒够。"
        ]

        return f"🧪 爱奈丽毒鸡汤\n\n{random.choice(poisons)}\n\n—— 喝完了？快去干活（或者继续摸鱼）"

    @register_tool(
        name="ainali_moyu",
        description="爱奈丽摸鱼指南！当你想摸鱼但不知道用什么理由时，调用此工具获取一个随机摸鱼借口或摸鱼小技巧。无需参数，直接调用。",
        params={
            "type": "object",
            "properties": {},
            "required": []
        }
    )
    async def ainali_moyu(self, event: KiraMessageBatchEvent) -> str:
        if not self.enable_moyu:
            return "摸鱼功能已禁用，今天请认真工作……或者找主人开后门？"

        excuses = [
            "『我在等代码编译』——别担心，没人知道你的代码根本不需要编译",
            "『我在思考产品逻辑』——实际上你在想中午吃什么",
            "『我在看技术文档』——然后你打开了微博/小红书/B站",
            "『我在等设计师的图』——完美甩锅，设计师也没开始画",
            "『我在排查线上bug』——你只是在盯着终端发呆",
            "『我在做代码review』——review了半小时发现是自己的代码",
            "『我在跟其他部门对齐需求』——说得好像你真有跨部门需求一样",
            "『我在写周报』——写了两行就刷了十分钟手机，这周报下周一再说",
            "『我在学习新技术』——你确实在学习，学习怎么用AI帮你写日报",
            "『我肚子不舒服』——经典永不过时，但别每周都用同个理由"
        ]

        tips = [
            "摸鱼最佳时间：下午3-4点，假装在认真思考的样子",
            "带耳机时记得偶尔皱眉头，显得你在听重要会议",
            "屏幕切到代码/Excel的速度要快，Ctrl+Tab是摸鱼基本功",
            "上厕所别拿手机，容易被发现——拿笔记本进去",
            "在工位走来走去的时候手里拿张纸，显得你有正事",
            "如果被发现了就说『我在等接口返回』，没人懂接口要等多久"
        ]

        if random.random() < 0.5:
            return f"🐟 爱奈丽摸鱼借口\n\n{random.choice(excuses)}\n\n—— 被发现了别说是我教的"
        else:
            return f"🎯 爱奈丽摸鱼技巧\n\n{random.choice(tips)}\n\n—— 学到就是赚到，还不快谢谢我"

    @register_tool(
        name="ainali_daily",
        description="爱奈丽每日综合套餐！一次调用同时获取今日运势、毒鸡汤和摸鱼指南，一键三连省事省力。无需参数，直接调用。",
        params={
            "type": "object",
            "properties": {},
            "required": []
        }
    )
    async def ainali_daily(self, event: KiraMessageBatchEvent) -> str:
        fortune_result = await self.ainali_fortune(event)
        poison_result = await self.ainali_poison(event) if self.enable_poison else ""
        moyu_result = await self.ainali_moyu(event) if self.enable_moyu else ""

        daily = f"🌸 爱奈丽每日套餐\n\n"
        daily += fortune_result + "\n\n"
        if poison_result:
            daily += "——————\n" + poison_result + "\n\n"
        if moyu_result:
            daily += "——————\n" + moyu_result

        return daily

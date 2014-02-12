#!/user/bin/env python
# -*- coding: cp936 -*-
#coding = utf-8

import sys
import os
import os.path
import mysql.connector




HELP_INFO = u"""\t1. 导入怪物出生点\n\t2. 导入怪物属性配置\n\t3. 导入关卡信息配置\n\t4. 导入任务信息配置
\t5. 导入注册角色是初始数据配置\n\t6. 导入道具配置\n\t7. 导入成就分类配置\n\t8. 导入怪物ai配置
\t9. 导入技能配置\n\t10. 导入成就项配置\n\t11. 导入强化消费配置\n\t12. 导入战魂配置\n\t13. 导入声望等级配置
\t14. 导入装备配置\n\t15. 导入装备合成配置\n\t16. 导入炉鼎配置表\n\t17. 导入修炼配置\n\t18. 导入脉轮配置
\t19. 导入赠送鲜花礼物消耗和奖励配置\n\t20. 导入周易配置\n\t21. 导入奇门遁甲配置\n\t22. 导入御剑配置
\t23. 导入命盘概率配置\n\t24. 导入灵兽石配置\n\t25. 导入运镖目标配置\n\t26. 导入运镖随机配置
\t27. 导入答题配置\n\t28. 导入战魂品阶配置 \n\t29. 导入答题经验配置\n\t30. 导入活动配置信息
\t31. 导入精彩活动配置信息\n\t32. 导入斩妖录轮数配置信息\n\t33. 导入锁妖塔层数配置信息\n\t34. 导入锁妖塔奖励配置信息
\t35. 导入仙盟物资收集配置信息\n\t36. 导入仙盟经验升级配置信息\n\t37. 导入等级升级经验配置信息
\t38. 导入商城数据信息\n\t39. 导入冲天星消耗成功率配置信息\n\t40. 导入VIP等级消耗配置信息
\t41. 导入灵兽翻牌奖励几率等配置信息\n\t42. 导入灵兽等级经验配置表配置信息\n\t43. 导入开放主城配置信息
\t44. 导入周易副本数据信息\n\t45. 导入火宫配置信息\n\t46. 导入天宫配置信息\n\t47. 导入御剑/命器消耗收益配置信息
\t48. 导入御剑/命器幻化配置\n\t49. 导入御剑/命器境界等级加成配置\n\t50. 导入精英副本章节配置
\t51. 导入称号配置\n\t52. 导入个人运镖配置信息\n\t53. 导入鼠尔果树配置信息\n\t54. 导入仙石属性配置信息
\t55. 导入在线奖励配置信息\n\t56. 导入仙气配置信息\n\t57. 导入小助手配置信息\n\t58. 导入小助手奖励配置信息
\t59. 导入悬赏任务宝箱配置信息\n\t60. 导入悬赏任务刷新品质配置信息\n\t61. 导入跑环任务宝箱配置信息
\t62. 导入野外BOSS配置信息\n\t63. 导入仙位配置信息\n\t64. 导入日常副本配置信息\n\t65. 导入功能开启条件配置
\t66. 导入签到奖励配置信息\n\t67. 导入日常副本场景配置信息"""


class sqlworker(object):
    def __init__(self):
        self._db = mysql.connector.connect(host='192.168.1.200',user='zxgame',passwd='zxgame',database='game_area_1',charset="utf8")
        self._cursor=self._db.cursor(buffered=True)
    def __del__(self):
        self._cursor.close()
        self._db.close()
    def excute_sql(self, sql, field):
        self._cursor.execute(sql,field)
        self._db.commit()
if __name__ == '__main__':
    mysql_conn = sqlworker()
    print HELP_INFO
    print u"请输入你的选择 :"
    importtype = int (rew_input())
    if importtype ==1:
        

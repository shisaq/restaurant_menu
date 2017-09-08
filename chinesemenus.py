# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///chineserestaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
restaurant1 = Restaurant(name="小四川")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(name="红糖凉糕", description="暑气渐来，这天气还是最适合喝碗凉糕消消暑，红糖的甜蜜混合凉糕的Q弹，简直是夏日酷暑里的一抹清凉的光景。",
                     price="$7.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name="红米鸡蛋肠粉", description="一直希望吃下广东美食，没想到自己在家也可以动手来做。印象中的肠粉好像是乳白的，没想到还有红色的肠粉，好吃又不费事的一道广东美食，动手试试吧！",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="红烧肉卤蛋", description="偶然的机吃到红烧肉卤蛋，自己研究了一番，搬出心爱的砂锅，炖出一锅红烧肉卤蛋，第一次就不够吃啦，有机会的话，一定要亲手做给家人吃一次哦。",
                     price="$5.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="老北京懒龙", description="懒龙是北方地区的特色饭食。经济实惠并且做工简单，比炒菜还简单，一个 简单的懒龙可以包含主食和菜，可供一家人食用，较为方便！",
                     price="$3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="芝麻红薯饼", description="红薯有长寿食品之誉，富含丰富的氨基酸，蛋白质，纤维素以及各种矿物质。红薯的吃法也是多种多样，除了冬季大街小巷的红薯飘香能让你垂涎欲滴，酥香可口的红薯饼也是一种哦。",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="咸蛋菜心粥", description="炎炎夏日，许多人没有食欲，不思饮食，这时候一杯解饿饱腹的粥便可解决问题，喝粥既简单方便又养胃，配以些许小菜，可以说很适合夏天食用了！",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="红豆手抓饼", description="酥软油润的红豆手抓饼是山东的有名小吃，用简单的材料，足不出户做出山东有名小吃，品尝山东特色，口感清甜滋润，老少皆宜。",
                     price="$.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="风琴土豆", description="风琴土豆是吃货们必不可少的小吃了，上学时和朋友必点！简单易做，好看有趣，考验你刀工的时候到喽，能把这种小吃做出不一样的味道就厉害了！",
                     price="$3.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="肉末笋丁炒粉丝", description="粉丝的劲道有嚼劲，配以春笋的清香可口，猪肉的新鲜口味，各种调料一起小火翻炒，绝对是这炎炎夏日里面的一场阳春白雪，令人心生食欲！",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(name="金阁")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="肉末酿豆腐", description="豆腐，中华传统美食，物美价廉。一盘成功的豆腐就要色香味俱全，当然，如何给素菜增添一点风味，就是肉沫酿豆腐啦！",
                     price="$7.99", course="Entree", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    name="咖喱鸡盖浇饭", description="咖喱、土豆、鸡块，这三样可以说是美食届的顶级搭配了，咖喱的浓郁、土豆的香甜、鸡块的鲜嫩，相信没有人能够抵挡的了这道咖喱鸡盖浇饭的美味了。", price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="家常蛋羹", description="上班族下班回来时间不多，当然是做些又省时间又简单的菜啦！ 这个菜绝对是偷懒的绝招！",
                     price="15", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="红糖凉糕", description="暑气渐来，这天气还是最适合喝碗凉糕消消暑，红糖的甜蜜混合凉糕的Q弹，简直是夏日酷暑里的一抹清凉的光景。",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="酱肉丁", description="盛夏酷暑，完全没食欲，总不能捧着冰淇淋过日子吧。肉类还是要有的，精致的酱肉丁配上香喷喷的米饭，拯救夏日的没胃口。",
                     price="14", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="蓝莓爆浆酸奶小蛋糕", description="蓝莓，浪漫又美味的水果，颜值高，营养价值高，搭配下午茶甜品小蛋糕再合适不过了，酸酸甜甜的，多吃一个也不会很腻，蓝莓蛋糕你会做了吗？",
                     price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Restaurant(name="​川湘汇")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="莓果冻酸奶", description="冰淇淋是夏天的标配，无论小朋友还是大朋友都爱吃，加上草莓树莓的清甜，给这款冻酸奶增色不少，老少皆宜，夏日精品！",
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="蛋包饭", description="把蛋炒饭做到美味精致是一件多么容易的事情，做一款蛋包饭，是家里小朋友偏爱的额营养早餐，轻松做个厨艺了得的好妈妈。",
                     price="$6.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="红萝卜青瓜沙拉", description="青瓜配上红萝卜，炎炎夏日的清凉食物之选，简单、低卡路里的食材，还能起到减脂的作用。简简单单的一道红萝卜青瓜沙拉作用一箭双雕。",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="糖醋鱼块", description="一条鱼能做出几道菜？鱼头鱼尾鱼身，完全可以做一桌大菜。鱼身适合怎么做，糖醋鱼块啊，鲜嫩多汁口感嫩，毕竟以就做出来一道美食。",
                     price="$6.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="南瓜花朵馒头", description="南瓜富含多种营养成分，可以利用南瓜制作的食物也非常多，这次介绍的这款南瓜花朵馒头，色泽艳丽，外观独特，适合家里有老人孩子的朋友们。",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(name="新府河")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="生煎包", description="生煎包往往是一看上去就很有食欲的小面点，制作起来也非常容易，去外面买不如自己做，可以说掌握这样一个美味早餐的烹饪技能非常有必要。",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="青汁花篮饺子", description="饺子可以各型各样，青汁料理也是花样百出，强强联合，这是一种编花篮式的饺子，让你从此爱上饺子。",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="家常虎皮青椒", description="香辣开胃，超级下饭，上班族回家很快就能做好。",
                     price="$4.50", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="青汁烤饼干", description="今天用青汁和面粉做了烤饼，使用材料很简单： 材料：面粉、青汁、玉米淀粉、奶粉、玉米油、白糖、蛋黄和盐。 方法很简单的，一看图就会，大家可以跟着动手操作一下，很好吃的！",
                     price="$6.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="韩国石锅拌饭", description="黄瓜：利水、清热、解毒 香菇：补虚、健脾、化痰 金针菇：补肝、抗癌、益肠胃。",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(name="巧克力派", description="巧克力派的原型也是有点叛逆，被认为不合群的三个好姐妹为自己组成的一个小集体，不和大家一起，只有三个人 。而现在，巧克力派则是rose之梦和塔罗银漫画组的公用吉祥物。",
                     price="$6.80", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(name="唐园")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="青汁冰饮——青汁星冰乐", description="青汁也能做星冰乐哦，非常的简单，大家可以试试哦。一杯很简单的青汁星冰乐特别适合夏天哦！生活五彩（冰）纷 ，健康美味享（瘦）~~",
                     price="$13.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="肥牛饭团", description="想要吃饭团，只是饭团怎么行？肥牛饭团+五彩，造型精美，食材丰富，营养均衡，而且饭团类的烹饪真的非常容易了，一学就会，好看又好吃，简直就是必备技能啊！",
                     price="$4.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="泡椒山药", description="山药营养丰富，常用于炖汤。但今天我想要带给大家的是一款泡椒山药。酸酸辣辣，十分爽口下饭。而且制作方法简单快手，不可错过的一道佳肴。",
                     price="$6.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="五彩豆腐", description="豆腐是传统美食，营养美味，价格实惠，家宴、过年必不可少。今天推荐的这款五彩豆腐，是高颜值高营养的一道美味，喜欢就别错过了！", price="$3.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="菠萝饭", description="菠萝饭是粤菜系中的经典饭之一。延续了广东的饮食，水果做菜，用菠萝的酸酸甜甜，再加虾米的酥香、鸡蛋的香滑，配一点蒜 、红辣椒、青辣椒。菠萝饭的重点在于要选择优质软糯的大米饭，菠萝不要太熟。",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(name="​家味")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="腊肉炒蚕豆", description="腊肉搭配什么菜都十分好吃，尤其是到了春天各种新鲜蔬菜上市，更是花样繁多。今天就做了一款腊肉炒蚕豆，腊肉浓香，蚕豆清甜，十分好吃。",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="双椒炒肉皮", description="肉皮含有丰富的胶原蛋白，是美容佳品，但很多人都会把它扔掉十分可惜。今天小编要推荐给大家一种新的肉皮做法，双椒肉皮，一起看看吧！",
                     price="$7.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="红辣椒炒肉丝", description="红椒含有丰富的维生素，搭配肉丝来炒制，色泽鲜艳，营养下饭。快来看看吧~",
                     price="$6.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="春笋焖排骨", description="春天正是吃春笋的好时节，这时的春笋鲜嫩爽口，搭配排骨一起红焖，营养美味，让人念念不忘，一起来看看这道菜怎么制作吧！",
                     price="$6.75", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="麻婆广茄", description="广茄是一种细长的茄子，皮薄肉嫩，十分好吃。今天就用广茄做了到麻婆广茄，麻辣鲜香，一次能吃五碗饭。",
                     price="$7.00", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Restaurant(name="天天见面")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(name="凉拌鸡蛋干", description="鸡蛋干想必大家都吃过，做法多种多样，今天做了一种最简单的方法，凉拌。凉拌鸡蛋干，爽口美味，佐粥佳品。",
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(name="爆炒高丽菜", description="五分钟做好一道美味营养的家常菜，这道菜就是爆炒高丽菜，高丽菜又叫包菜、卷心菜，含有丰富维生素，并且热量极低哦~",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="红烧猪皮", description="猪皮，平时在买猪肉的时候就会让人去掉，要不就是买一些猪皮回来做猪皮冻，这款红烧猪皮，还是第一次做的，味道真的不错哦！",
                     price="$10.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="山楂陈皮饮", description="之前吃橘子的时候，收集了不少橘皮，凉干后就是陈皮了，陈皮的作用不少，和山楂一起做的这道山楂陈皮饮，酸酸甜甜的，很是开胃。",
                     price="$7.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="缅芫荽炒豆芽", description="缅芫荽也叫刺芹，以前在乡下的时候，奶奶会用它来做菜，奶奶说它是一个“宝”不但好吃，对很对病都有一定的治疗作用。",
                     price="$8.95", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(name="肘子肉炒榨菜", description="肘子肉酱好后用来做炒菜吃，真的很美味，以前在家的时候妈妈就会这么做，不说了，还是快点和大家分享这道令人胃口大开的下饭菜吧！",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(name="猪肉丸烩茄子", description="猪肉丸烩茄子，头一次这么吃哟。",
                      price="$1.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Restaurant(name="鼎味")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="凉拌脱水菜芯", description="简单方便，还能感受来自脱水蔬菜别样的风味和魅力。",
                     price="$5.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="清炒萝卜片", description="使用脱水白萝卜，口感清脆，挑动你的味蕾。 白萝卜中含有丰富的维生素和微量元素，可以增加人体的免疫力。",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(name="Q和J的餐厅")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="醋焖鸡", description="鸡腿肉和米醋的碰撞与交流！",
                     price="$5.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(name="麻婆豆腐", description="Trader Joe's的嫩豆腐加上意大利烤肠末，被花椒引导得恰到好处~",
                     price="$6.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(name="番茄炒蛋", description="中国国菜，简单效率，好吃不贵！",
                     price="$4.25", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


print "added menu items!"

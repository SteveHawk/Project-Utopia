# Project Utopia

### 这是什么

Project Utopia 是一个我个人的学习项目。如果代码丑 / bug 多也请多见谅。

这个项目首先是对于一个 PNP (Print and Play) 游戏 Utopia Engine 的代码化工程。

其次这个项目是一个用来给我提供学习强化学习算法的平台。目前已经开始尝试了蒙特卡洛树搜索，以后可能还会有更多。

### 如何运行

Utopia Engine 文件夹下的 main.py 为乌托邦引擎的游戏入口。

Monte Carlo 文件夹下的 MCTS.py 为蒙特卡洛树搜索的入口。

### 关于 Utopia Engine

乌托邦引擎是一个免费的打印即玩（PNP, Print and Play）游戏，我个人理解为一个单人的桌面角色扮演游戏（TRPG）。原作者为 Nick Hayes，目前没有找到相关的版权信息，如有侵权请联系我。

游戏简介：<https://boardgamegeek.com/boardgame/75223/utopia-engine>

官网下载：<https://nevermoregames.com/downloads>

游戏规则在官网下载的压缩包里有英文版的 Rulebook。在知乎上有非常详细的中文翻译，详见以下链接：

<https://www.zhihu.com/question/26553706/answer/55915290>

<https://www.zhihu.com/question/26553706/answer/56691434>

两个知乎回答的所有权均归原作者所有。

### 关于蒙特卡洛树搜索

简介可以看下我的博客，前一阵写了个入门学习的笔记：

<https://www.cnblogs.com/stevehawk/p/8870144.html>

里面引用了很多博客、维基等内容，所有引用内容版权均归原作者所有。

现在已经写的蒙特卡洛树的代码来自于<www.mcts.ai>，Python代码链接为 <http://mcts.ai/code/python.html>。网页上给出的是 Python 2 的代码，我在 Monte Carlo 文件夹下的 MCTS-sample.py 中把它转换成了 Python 3 的代码。

### 开发计划

目前的计划是先把整个游戏代码化。初步代码化结束以后会进行代码结构的优化，毕竟现在的代码又丑又乱。优化的差不多了可能会开发 GUI，说不定还会搬到网站上可以在线玩的那种。

然后就是会开发一个机器人，用（深度）强化学习来玩这个游戏。目前已经写的蒙特卡洛树的部分仅仅玩了那一个六个格子填数字的游戏，至于整个游戏能不能玩的来还不知道，不过锅先摆在这。

### *另外*

就在写这个 readme 的时候，我惊奇的发现乌托邦引擎竟然有续集。链接如下：<https://boardgamegeek.com/boardgame/193105/utopia-engine-beast-hunter> 如果以后有机会，我一定会去好好探个究竟。


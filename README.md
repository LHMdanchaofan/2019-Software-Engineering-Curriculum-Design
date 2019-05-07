<h1 align='center'>2019 计科1605班软件工程课程设计</h1>
<div align='center'>
五一节后最新进展。New Version, new design and new features... Happy coding and hacking. 
</div>
<div align='center'>
组长：罗登、蔡锐 、张云皓、何显、朱迪迪
</div>

<br>


## 查看运行效果

### 登录
![login_form](EMS/static/img/readme_img/login.png)

### 初始界面
![first_login](EMS/static/img/readme2/first_login.gif)

### 后台管理-查看个人信息

![personal_info](EMS/static/img/readme2/personal_info.png)

### 成绩管理-查看专业计划
![view_major_plan](EMS/static/img/readme2/view_major_plan.gif)

### 成绩管理-查看专业课程

![view_major_course](EMS/static/img/readme2/view_major_course.gif)

### 成绩管理-查看个人成绩

![view_person_score](EMS/static/img/readme2/view_person_score.gif)


### 成绩管理-查看个人学业情况

![view_person_study](EMS/static/img/readme2/view_person_study.gif)

### 成绩管理-教学评价

![access_teacher](EMS/static/img/readme2/access_teacher.gif)

### 毕业设计-浏览选题
![grad_view_project](EMS/static/img/readme2/gradu_project_view.gif)

## 关于角色和如何登录

### 角色分类

系统总共有三类角色：学生、教师、管理员，均采用继承和扩展Django自带User类的方式实现。

- 学生，采用默认字段username为学号。同时默认密码password与学号相同（在存入数据库时实现了加密）。（默认学号为10位，不可修改）
- 教师，采用默认字段username为工号。同时默认密码password与工号相同（在存入数据库时实现了加密）。（默认工号为9位，不可修改）
- 管理员，默认为Django superuser。可以通过`python manage.py createsuperuser`命令创建。

### 如何获取

**强烈建议通过Django ORM方式获取所关心的信息，而不要去数据库中疯狂操作**。

```
In [1]: from backstage.models import Student, Teacher

In [2]: Student.objects.first()
Out[2]: <Student: 2016000001-孙章衡>

In [3]: Teacher.objects.first()
Out[3]: <Teacher: 201100001-兰金叻>

In [4]: len(Student.objects.all())
Out[4]: 649

In [5]: len(Teacher.objects.all())
Out[5]: 1033
```

### 管理员登录

管理员使用了Django中的`superuser`类，属于User。默认创建了10个管理员，已经导入到最新的`ems.sql`文件中。用户名默认为`superuser[1-n]`，如`superuser1`，密码同用户名。
也可以通过以下脚本插入


## 不同角色视图说明

采用Django模板继承机制实现不同角色看到的视图不同。在templates文件夹下有四个文件分别为`base.html`,`student_base.html`,`teacher_base.html`,`adm_base.html`。其中`base.html`为所有的基础模板，定义了界面的基准色调，和左侧Slider Bar，顶部导航栏，登录头像，登录状态提示，登出等。
其他三个文件分别继承于`base.html`，并且自定义了自己的Slider Bar和顶部导航栏。其于各个模块中的`html`文件均继承于上述三个文件，确保了不同的角色登录看到的功能均不相同。

其于子模块子需要在`{% block content %} {% endblock %}`内部书写`<section></section>`内容即可。

## 工作安排

### 后台管理

**职责说明**：

>**维护**校内所有学生和教师信息、**维护**所有的课程信息、**维护**所有的教室信息。
管理教务管理系统的不同类型的用户账号，进行**权限维护**。发布各类**通知**信息。为系统的使用提供帮助，以及模板**文档的下载**。实现不同用户组的**邮件群发**。对成绩达不到毕业要求的学生，发出**学位警告通知**。

- [x] 关于基础表格的属性和字段已经创建完毕。并且成功导入相应的数据。方便轻松导入。
- [ ] 全校教室表还没有导入对应数据，这个需要与排课小组详细讨论确定结果。教室的**容量余量**等信息会影响排课。
- [ ] 完成前后端交互的对教室、教师、学生的增删改查的功能。对于增删改要求使用Ajax异步交互的方式，与后端交互验证。不能直接找不到报错或者重复报`DoesNotExiest`或者`Integrity Error`。[参考代码](https://github.com/RonDen/2018DBDesign/tree/FirstKind/templates)。
- [ ] 完成学生和老师的批量导入功能。系统不提供直接的前台注册功能（不符合教务管理系统的性质），而是直接批量导入。通过Excel表格导入（建议使用Pandas）或者数据库脚本插入。要求提供前端交互界面，Excel模板下载方法。[参考代码](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/master/EMS/utils/database_utils)
- [ ] 完成邮件功能。群发和单发。[参考代码](http://www.liujiangblog.com/course/django/175)
- [ ] 完成系统通知发送和显示功能。可以参考博客或类似评论系统的实现。


### 成绩管理

**职责说明**：

> 成绩管理子系统管理学生的**课程成绩**并提供**课程评价**功能。教师可**提交成绩**，**打印成绩**，**下载成绩**汇总。学生可**查看课程成绩**，查看个人已选课程成绩汇总信息，并可下载打印。最后系统应能够向管理员提供**查询界面**和**各类报表**，**统计**学生成绩情况。系统提供基于Web的访问，同时支持学生通过手机查看个人成绩。


- [x] 课程信息的构建。
- [x] 学生课程成绩信息的构建。包括数据的导入。
- [x] 实现教学评价功能。
- [ ] 完善评教功能，评教和查询成绩的约束。查看成绩需要完成评价。
- [x] 实现按学号筛选，找到学生选修的课程以及对应成绩得分。包括平时分和最终考试得分。实现学生的个人成绩查询。
- [x] 实现学生个人的成绩汇总和分析界面。
- [ ] 实现教师通过Excel表格上传成绩的功能。提供上传成绩的Excel表格模板下载地址。
- [ ] 提供老师对自己所教学班级的成绩分析功能。根据老师筛选出所教课程，并在界面上显示各个班级的成绩情况（需要展现出重要统计信息，如平均分，不及格率、优秀率等，绘制相应的分布图表。直方图和饼图）。在此页面提供导出PDF和班级成绩Excel表格的功能。导出方便打印或进一步分析。
- [ ] 提供关于专业和行政班的查询和统计分析功能。导出成绩信息为Excel表，便于辅导员等相关人员进行分析。
- [x] 实现了系统管理员查询、修改、删除成绩数据的功能。
- [ ] 完善系统管理员查询功能，添加下拉框查询，提供各**专业**级别的成绩统计分析功能。
- [ ] 向系统管理员展示各个专业年GPA走势，绘制相应的图表（分布图和趋势图）。提供导出图表功能PDF和Excel。
- [ ] 对不同角色跳转的功能，避免学生通过path进入管理员或者教师的界面。（已经在session中记录了用户type）

### 排课子系统

**职责说明**：

> 为教师教授的课程安排教室和上课时间。一个教师在一个学期可能承担多门的课程，这些课程的时间不应冲突。一个教室在同一时间只能安排一门课程。教务管理人员登录后，可以进行排课，查询教室使用情况，教师课程安排情况，还可以临时为一些教学活动安排教室。学生登录，可以查看每门课的上课时间和地点。教师登录可以看到个人承担课程的上课时间和地点，可以查看某个专业的推荐课表，其他教师的课表等。系统应能够向管理员提供查询界面和各类报表，统计排课情况。系统提供基于Web的访问，同时支持教师和学生通过手机APP查看排课情况、考试时间地点。

- [ ] 完成排课所需要的数据结构和数据库表格的创建。
- [ ] 实现排课算法。
- [ ] 提供对空闲教室的前端查询功能。这个功能对学生、教师、管理员都需要提供。
- [ ] 完成手动排课前端交互功能（要求界面友好，拖拽式等）。
- [ ] 对管理员提供借教室，也就是将空闲教室修改为占用的功能。用于安排临时教学活动。标明占用时间。

### 选课子系统

**职责说明**：

>课程分为研究生课程和本科生课程；也可以分为必修、选修、辅修。学生以学号和密码登陆，系统显示用户已选的课程、用户有权选但未选的其他课程，并显示具体信息（如学分）。学生选择后，系统根据规则检查用户是否进行正确的选课（如时间冲突、跨专业选课等）；如果错误提示用户改，否则修改选课数据库。教师可以查看自己所教授课程的选课情况，下载选课名单。最后系统应能够向管理员提供查询界面和各类报表，统计每门课的选课情况。系统提供基于Web的访问，同时支持学生通过手机APP选课。

- [x] 设计并实现完成选课需要的数据结构和数据库表格。提供对应的测试数据。
- [ ] 设计学生选课的界面。要求异步交互提示。
- [ ] 为教师提供选课名单。
- [ ] 向管理员提供选课情况分析报表。


### 毕业设计子系统

**职责说明**：

>管理毕业设计选题和成绩。教师可以提交多个毕业设计题目，描述题目要求和对学生的要求。学生可以浏览教师发布的毕业设计题目，进行选择。在学生完成选择后，针对每个题目教师确认选择一个学生。学生向系统提交毕业设计各种文档。教师可以查看学生提交的毕业设计文档，提交毕业设计最后成绩。最后系统应能够向管理员提供查询界面和各类报表，统计毕业设计选题情况和学生成绩。系统提供基于Web的访问，同时支持学生通过手机APP查看选题和查看成绩。

- [x] 完成毕业设计系统涉及到的数据库表格的设计和创建。
- [x] 学生浏览题目并选择题目的界面。（要注意权限和验证，是否是跨专业，是否可以跨专业。选多个的错误提示。选题截至时间的显示。选完题之后要求系统自动发送通知到对应用户消息箱）。
- [ ] 学生在系统上提交相应文档。可以使用`FileField`。[参考代码](http://www.liujiangblog.com/course/django/95)
- [ ] 教师界面的实现。发布课题。查看多少人选了自己的课题。多少课题未选。
- [ ] 教师能够查看学生提交的文档（是直接在浏览器查看还是下载查看？`.docx`文档和压缩包文档可能无法实现浏览器查看。是否包含图片文件？`ImageField`，保存路径等）
- [ ] 管理员实现总体的（或者专业级别，老师级别的）毕业设计选题分析查询的界面和分析图表。



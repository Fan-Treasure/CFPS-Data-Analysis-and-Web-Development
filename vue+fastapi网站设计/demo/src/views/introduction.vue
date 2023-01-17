<template>
  <div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
      <el-submenu index="2" style="margin-left:3%">
        <template slot="title"><i class="el-icon-reading"></i> 目录</template>
        <el-menu-item index="2-1" style="color: black;"><a href="#title">title</a></el-menu-item>
        <el-menu-item index="2-2" style="color: black;"><a href="#title2">做饭用水</a></el-menu-item>
        <el-menu-item index="2-3" style="color: black;"><a href="#title3">收入水平</a></el-menu-item>
        <el-menu-item index="2-4" style="color: black;"><a href="#title4">工作水平</a></el-menu-item>
        <el-menu-item index="2-5" style="color: black;"><a href="#title5">教育水平</a></el-menu-item>
        <el-menu-item index="2-6" style="color: black;"><a href="#title6">统计学方法分析</a></el-menu-item>
        <el-menu-item index="2-7" style="color: black;"><a href="#title7">结论与建议</a></el-menu-item>
      </el-submenu>
      <el-menu-item index="3"  class="loginbu"  @click="tiaozhuan"><i class="el-icon-thumb"></i>登录/注册
      </el-menu-item>
    </el-menu>
    <div class="title" id="title">
      <div class="wenzi">
        <h1 class='main_title'>城乡差距与乡村振兴的碰撞</h1>
        <h1 class='second_title'>——实现地区平衡长路漫漫</h1>
        <div class="fangwen" style="display: flex;">
          <p>访问量：{{fangwen}}</p>

        </div>
      </div>
    </div>
    <div class="zhengwen">
      <p><b>城乡差异，地区差异一直是一个热点问题。</b></p>
      <br>
      <p>特别是随着经济的发展，中国经济在城市农村、不同地域发展的差距越来越大。城乡差距不仅体现在<b>经济</b>上，还体现在<b>政治</b>上。农村家庭和城市家庭之间的收入、资产、消费水平以及结构等情况也发生了不同。</p>
      <br>
      <p>本文的研究立足于<b>中国家庭追踪调查数据CFPS</b> 2010
        -2018年的数据。先后对中国家庭城乡差异化、城乡不同地区差异化<b>进行分析研究，找出差异化的内容以及水平程度，并寻找造成这种差异化的原因，最后得出本文的研究结论，并针对中国家庭的差异化发展提供建议。</b>以及如何缩小城乡差距、构建乡村振兴提供建议。
      </p>
      <br>
    </div>
    <div class="charts">
      <div id="main15"></div>
    </div>
    <div class="title-2" id="title2" ref="title2">
      <h1 :class='{main_title2:true,xianshi3:sig2==true}'>做饭用水</h1>
      <h1 :class='{second_title2:true,xianshi3:sig2==true}'>从百姓的基本需求洞见城乡差异</h1>
    </div>
    <br><br><br>
    <div class="charts">
      <div id="main1"></div>
    </div>
    <div class="zhengwen">
      <br>
      <p style="text-align: center;">2010-2018年城乡家庭做饭用水对比图</p>
      <br>
      <p>家庭基本生活条件<b>主要是做饭用水</b>，该方面可以看出基本家庭的生活条件。</p>
      <br>
      <p>
        城市几乎都是用的<b>自来水</b>做饭，并且2010到2018年做饭用水的来源基本没有变化。反观农村，自来水虽然占比40%-60%，但还有30%-50%的家庭用<b>井水</b>来做饭。不过，2010-2018年，农村家庭自来水做饭的占比<b>有所增加</b>，特别是2018年增幅很大，可见农村家庭的卫生情况<b>有所改善</b>。
      </p>
      <br>
      <p>接下来是不同地区城乡生活用水差异。下图中所示的南北部，东中西东北部的省份、直辖市、自治区的划分全部按照国家标准。</p>
      <br>
      <h3>南北部地区差异分析</h3>
      <br>
    </div>
    <div class="charts">
      <div id="main2"></div>
    </div>
    <div class="zhengwen">
      <br>
      <p style="text-align: center;">2010-2018年南北部城乡家庭生活用水对比图</p>
      <br>
      <p>
        无论是南部还是北部地区，城市做饭用水几乎都是<b>自来水</b>，很少家庭会使用井水等水源。至于农村地区，自2010年以来，使用自来水的家庭<b>逐年增加</b>，且南北部<b>都有所增加</b>，地区之间并没有存在显著的差异。可能由于近年来南北乡村地区都安装自来水管道，并且政府和家庭都对饮用水健康情况做出了管理。
      </p>
      <br>
      <h3>东中西部地区差异分析</h3>
      <br>
      <p>刚刚分析了南北部的做饭用水的差异，现在来分析中东西东北部地区的做饭用水差异，特别是农村地区。</p>
      <br>
    </div>
    <div class="charts">
      <div id="main3"></div>
    </div>
    <div class="zhengwen">
      <br>
      <p style="text-align: center;">2010-2018年中东西东北部城乡家庭做饭用水对比图</p>
      <br>
      <p>城市方面，东部和东北部地区使用自来水的比例<b>多于中部和西部</b>，城市中主要是西部和中部还有部分家庭在用井水做饭，可能由于和水源的存储有关。</p>
      <br>
      <p>
        农村方面，可以看出，在自来水和井水占比方面，西部农村和中部农村井水的比例在2010年时<b>高于自来水</b>，到2018年时自来水的使用比例更大。但是东部地区的农村家庭，一开始自来水的使用占比就多于井水的使用。而东北部农村近年来做饭用水的<b>变化不大</b>。此外，西部地区还存在使用窖水做饭的情况。说明中国农村的生活用水的习惯差异方面还有<b>极大的不平衡</b>。
      </p>
      <br>
    </div>

    <div class="title-3" id="title3" ref="title3">
      <h1 :class='{main_title3:true,xianshi3:sig3}'>收入水平</h1>
      <h1 :class='{second_title3:true,xianshi3:sig3}'>从人们的“钱袋子”中发现奥秘</h1>
    </div>
    <div class="zhengwen">
      <br>
      <h2>收入水平差异</h2>
      <br>
      <p><b>城乡收入水平的差距一直是国家和社会关注的重点对象，接下来通过家庭总收入和家庭人均收入两个方面的对比来逐步分析这种差异的来源。</b></p>
      <br>
      <h3>城乡家庭总收入对比</h3>
      <br>
      <p><b>通过对比城乡家庭的总收入水平。可以大致了解到城乡发展不均衡问题的程度。</b></p>
      <br>
    </div>
    <div class="charts">
      <div id="main4"></div>
    </div>
    <div class="zhengwen">
      <br>
      <p style="text-align: center;">2010-2018年城乡家庭总收入对比</p>
      <br>
      <p>
        近几年来城乡家庭的总收入<b>均翻了很多倍</b>。但是可以看出，收入的总体水平在城乡之间的<b>差距也被拉大了。</b>在2010年，城乡家庭的收入差距<b>不足2万</b>，到了2018年，城乡家庭之间的收入差距<b>已接近7万</b>。这中间的差距非常大，一个城市家庭的总收入差不多相当于<b>两个农村家庭</b>的总收入。
      </p>
      <br>
      <h3>城乡家庭人均收入对比</h3>
      <br>
      <p>
        从2012至2018年，无论是城市还是农村，收入水平都<b>显著性的提高</b>了。农村的人均收入增加了<b>近3倍</b>，城市的人均收入增加了<b>近2.6倍</b>。但是城乡人均收入水平差距从最开始的一万，增加到了<b>2.3万左右</b>。可见，几年来人均差距就如此之大。城乡之间的贫富差距岁随着经济的发展进一步加快，<b>即便经济增长放缓，差距也进一步增加。</b>
      </p>
      <br>
    </div>
    <div class="charts">
      <div id="main5"></div>
    </div>
    <div class="zhengwen">
      <br>
      <p style="text-align: center;">2012-2018年城乡家庭人均收入对比</p>
      <br>
      <p>
        从2012至2018年，无论是城市还是农村，收入水平都显著性的提高了。农村的人均收入增加了近3倍，城市的人均收入增加了近2.6倍。但是城乡人均收入水平差距从最开始的一万，增加到了2.3万左右。可见，几年来人均差距就如此之大。城乡之间的贫富差距岁随着经济的发展进一步加快，即便经济增长放缓，差距也进一步增加。
      </p>
      <br>
      <h3>分地区收入水平差异化研究</h3>
      <br>
    </div>
    <div class="charts_ditu">
      <div id="main6"></div>
      <div style="margin-left:20%">
        <el-button type="primary" @click="qiehuan">切换样式</el-button>
      </div>
    </div>
    <br>
    <br>
    <div class="zhengwen">
      <br>
      <p style="text-align: center;">2018年中国各省份居民人均可支配收入</p>
      <br>
    </div>
    <div class="charts">
      <div id="main7"></div>
    </div>

    <div class="zhengwen">
      <br>
      <p style="text-align: center;">南北部城乡家庭总收入</p>
      <br>
      <p>南部的收入水平均高于北部，并且这种差距在城市间的差距最大，2018年城市南部地区比北部地区人收入<b>高了7万</b>左右。农村在南北部之间的差异相比城市间差别<b>不是很大</b>。接下来观察下南北部家庭总收入的差距。
      </p>
      <br>
    </div>
    <div class="charts">
      <div id="main8"></div>
    </div>

    <div class="zhengwen">
      <br>
      <p style="text-align: center;">东中西部城乡家庭总收入差异</p>
      <br>
      <p>一方面，不论是农村还是城市，东部地区东部家庭总收入<b>大于</b>中部家庭总收入，中部家庭总收入<b>大于</b>西部、东北部总收入。</p>
      <br>
      <p>
        东部农村2012年家庭总收入最开始和中部<b>齐平</b>，和西部也差距不是很大，但是2018年，东部已经<b>远远超过</b>了中部和西部的收入。西部和中部的家庭总收入水平相差<b>不是很大</b>。东部家庭总收入水平比中西部<b>多2万多。</b>
      </p>
      <br>
      <p>东部地区是城乡收入差距最大的地区。2018年，东部地区的城乡收入差距<b>接近8万</b>，中部、西部、东北部地区差距则为3万至5万元。可能是由于西部整体的收入水平比较低下。同时，随着年份的增加不同地区的城乡差距也在增加。
      </p>
      <br>
    </div>


    <div class="title-4" id="title4" ref="title4">
      <h1 :class='{main_title4:true,xianshi3:sig4}'>工作水平</h1>
      <h1 :class='{second_title4:true,xianshi3:sig4}'>从职业模式的视角探究城乡发展</h1>
    </div>
    <div class="zhengwen">
      <br>
      <h2>成人工作单位性质差异化分析</h2>
      <br>
    </div>
    <div class="charts">
      <div id="main9"></div>
    </div>
    <div class="zhengwen">
      <br>
      <p style="text-align: center;">城乡工作单位性质差异图</p>
      <br>
      <p>
        从城乡工作单位类型整体可以看出，城镇居民<b>从事国企与外商工作</b>的比例高于农村居民。而农村居民<b>从事私营个体经济与政府工作</b>的比例高于城镇居民。由于农业生产的自然条件、农村历史上形成的自然经济传统使农村的生产方式以及从事的产业与城镇具有差异。
      </p>
      <br>
      <p>从产业方面来看，其中乡村居民主要从事的是相应的<b>第一产业</b>; 城市居民从事的是相应的第二和第三产业也就是<b>工业和服务业。</b></p>
      <br>
      <p>从政府政策方面来看，为了减少城乡工作差异和提高居民生活质量政府的政策会<b>偏向于农村</b>，为农村带来了许多工作福利。</p>
      <br>
      <h2>分地区对比城乡工作单位性质差异</h2>
      <br>
      <h3>a.南北部</h3>
      <br>
    </div>

    <div class="charts">
      <div id="main10"></div>
    </div>

    <div class="zhengwen">
      <br>
      <p style="text-align: center;">南北部城乡工作单位性质差异</p>
      <br>
      <p>城市之间，南北部的工作单位性质差异性<b>较农村地区大</b>，但两者在南北部工作类型上都具有差异。由于我国南北双方所处的地理位置、气候特征等方面的不同，造成了我国南北方工作类型的差异。</p>
      <br>
      <p>从自然地理角度来看，北方相对来说大部分处于<b>温带季风气候区</b>，南北方具有一定的气候差异致使南北方工作具有差异。</p>
      <br>
      <p>从交通运输角度来看，南北方交通运输具有差异。北方以<b>公路</b>为主。南方<b>路水联运</b>，商品销路比较好，适合发展外商，因此南方城乡外商工作比例明显高于北方。且南方城镇外商工作比例高于农村外商比例。</p>
      <br>
      <p>从其他角度来看，北方历来是中国的<b>政治中心</b>，北方政治较为活跃，国有企业数量较多，因此北部国企工作比例高于南方。<b>“北方多出当官，南方多出经商”</b>，这两句话较好地反映了南北方不同的在政治、经济上的差异。
      </p>
      <br>
      <h3>b.东中西部地区城乡差异分析</h3>
      <br>
    </div>

    <div class="charts">
      <div id="main11" ></div>
    </div>

    <div class="zhengwen">
      <br>
      <p style="text-align: center;">城乡东中西部工作性质对比</p>
      <br>
      <p>城市和农村都是西部在<b>政府单位工作</b>的偏多。</p>
      <br>
      <p>从自然因素来看，由于地理位置的原因，东部和中部<b>多平原和河流</b>，土壤肥沃，农业发达，是全国商品粮、商品棉基地集中地；同时东部和中部交通运输也较便利，因此城乡东部和中部的<b>私营个体</b>工作比例较西部高。
      </p>
      <br>
      <p>
        从经济因素来看，经济发展东部沿海发达东部城市发展快，东部大部分地区都是<b>沿海地区</b>，来自国外的资金以及能源比较多，外资经济发展上较西部便利，因此在外商工作上东部和中部的比例明显高于西部，且中部和东部的城镇居民<b>从事外商工作</b>比例高于农村。
      </p>
      <br>
      <p>从历史因素看，东北曾是我国的<b>重工业中心</b>，其城镇居民在国企工作的比例较高。</p>
      <br>
    </div>

    <div class="title-5" id="title5" ref="title5">
      <h1 :class='{main_title5:true,xianshi3:sig5}'>教育水平</h1>
      <h1 :class='{second_title5:true,xianshi3:sig5}'>城乡差异蕴藏于“百年大计”</h1>
    </div>
    <div class="zhengwen">
      <br>
      <p>随着经济实力的不断发展和人民生活水平的发展提高，我国贫富差距明显增大，并且呈现进一步扩大的趋势。为之而来的城乡差异也更为明显，而这种差距不仅仅表现在经济上，在城乡教育问题上也十分突出。致使城乡教育之间存在的巨大差距。
      </p>
      <br>
    </div>
    <div class="charts">
      <div id="main12"></div>
    </div>

    <div class="zhengwen">
      <br>
      <p style="text-align: center;">城乡居民教育水平对比图</p>
      <br>
      <p>
        城乡居民教育水平呈现巨大差异。其中农村居民教育水平<b>大部分在大专以下</b>，小学文凭、初中文凭与高中文凭则占多数，文盲与半文盲比例<b>明显高于</b>城镇比例。城市居民<b>教育水平总体偏高</b>，大都具有高中及以上学历，文盲与半文盲比例只有<b>农村比例的一半</b>。
      </p>
      <div style="display: flex;">
        <img class="img01" src="https://s3.bmp.ovh/imgs/2022/02/202f851995506b80.jpg" alt="">
        <div>
          <br>
          <p>从<b
              class="tuchu">城乡教育资源分配</b>的角度来看，我国自实行义务教育以来，虽然国家和政府做了许多努力，但义务教育的城乡差距依然存在。很多农村地区<b>九年制义务教育得不到保障</b>，且农村教育设施及条件较差，农村的教育资源稀缺，<b>乡村教师资源较城市贫乏，</b>教师素质也偏低。城市学校众多，且形成了良性竞争的环境，有助于提高教育水平，乡村学校少，科目单一，师资力量不足，且需要教育支援。在城市的孩子相对来说见识多，视野开阔，思维活跃，应变能力较好。在城市的孩子相对来说会有更多的时间、机会来学习更多的知识，父母的指导、各种培训机构、各种网上资料、图书馆等资源。且城市中的学生，享受不断升级换代的教育设施，选择自己所喜爱的课程，接受素质教育。相对城市，农村的孩子一直接受着劣等的教育，可能将农村居民的低素质持续下去，造成长期性的城乡差距。
          </p>
          <br>
        </div>
      </div>
      <p>从<b
          class="tuchu">经济方面</b>而言：经济是教育发现的一个基本因素。地区经济的发展不平衡造成不同地区之间受教育程度的不平衡，城镇经济发展较农村先进。因此城镇居民教育程度普遍高于农村居民教育水平。根据需要假说解释，人只有基本需要得到满足，才能发展高层次需要，城市的经济发展水平的到了基本满足，从而人们的基本生活需求也就得到满足，他们会追求下一个需求，就会更加注重教育等方面的发展开始这一方面的消费，而乡镇的经济还有待发展，故而他们会先满足基本需求，换一句话说就是：城市的人他们已经过了吃好喝好的阶段（比吃饱喝饱高一个阶段）了，就开始对自己内外及外在美的需求，而乡镇人们想的是我先吃饱，吃好。
      </p>
      <div style="display: flex;">
        <div style="margin-top: 5vh;">
          <br>
          <p>从<b
              class="tuchu">科技方面</b>而言，现在的教育离不开科技的发展，现代教育技术已经充分在城市应用。城市的孩子可以通过<b>互联网</b>学习到更多的东西，从一个小的角度出发，在城市，学校教师利用互联网技术，可以将课堂变得更加有趣生动贴切，把枯燥乏味晦涩的知识更加生动的呈现给学生，那么学生的动力就提高了，而在乡镇，这些技术没有得到普及，那么学生在面对同一知识点的时候，就只能死记硬背了，所以付出同样的努力，城市教育水平会更高。
          </p>
          <br>
        </div>
        <img class="img02" src="https://img1.imgtp.com/2022/02/12/5IC1YvKv.jpg" alt="">
      </div>
      <p>从<b
          class="tuchu">教师分配与师资力量</b>而言，所谓人往高处走，水往低处流，大多数优秀老师更希望在城市发展，而不是乡镇，教师水平不一样，那么教育水平自然不一样。现在农村学校有相当一部分教师是民办转公办或村聘教师,相当一部分教师存在<b>教法陈旧、观念落后</b>等问题。教师队伍整体存在着<b>年龄偏大、知识结构老化、知识面窄</b>的问题。面对新形势下的素质教育，面对<b>改革后的义务教育新课程</b>,他们往往显得力不从心。
      </p>
      <br>
    </div>

    <div class="charts">
      <div id="main13"></div>
    </div>

    <div class="zhengwen">
      <br>
      <p style="text-align: center;">南北部城乡居民教育水平对比</p>
      <br>
      <p>从南北部城乡居民教育水平对比图中可以看出，南部城乡居民的教育水平<b>普遍高于</b>北部城市，且南北部农村居民的教育水平差异大于南北部城市居民的教育水平。北部农村居民文盲与半文盲数量<b>高于城镇几乎一倍</b>。
      </p>
      <br>
      <p>从南北方发展水平来分析，南北方在经济发展水平不均导致出现教育差距，南方经济较北方发达，因而南方居民教育程度<b>明显高于</b>北方居民。</p>
      <br>
    </div>

    <div class="charts">
      <div id="main14"></div>
    </div>

    <div class="zhengwen">
      <br>
      <p style="text-align: center;">东中西东北部城乡居民教育水平对比</p>
      <br>
      <p>
        东部城市，中部城市以及东北部城市居民<b>教育水平明显高于</b>西部居民的教育水平。西部地区城乡居民处于在<b>文盲与半文盲</b>学历以及小学文凭的人数较多，在农村尤为明显。其次，东部地区城乡居民<b>大都具有中高等学历</b>。低学历人口的比例农村远远高于城市，高学历人口的比例则是城市<b>明显高于农村</b>。
      </p>
      <br>
    </div>

    <div class="title-6" id="title6" ref="title6">
      <h1 :class='{main_title6:true,xianshi3:sig6}'>统计学方法分析</h1>
    </div>
    <div class="zhengwen">
      <br>
      <p>通过统计描述分析，可以看得出中国农村间存在明显的地域收入差距，接下来用具体的检验方法来验证这种地区是否导致收入差距的显著性检验。先进行<b>相关性分析</b>。结果如下。</p>
      <br>

      <div style="margin-left:20%">
        <el-table :data="tableData" style="width: 60%">
          <el-table-column prop="date" label="家庭总收入地区">
          </el-table-column>
          <el-table-column prop="name" label="东中西部">
          </el-table-column>
          <el-table-column prop="address" label="南北部">
          </el-table-column>
        </el-table>
      </div>
      <br>
      <p align="center">表3-1农村地区与收入相关分析</p>
      <br>
      <p>从以上表3-1农村地区与收入相关分析可以看出，地域与收入之间的确存在相关关系，但是东中字西部的地域差异和收入之间的相关关系不显著，南北部地域差异和家庭收入之间的相关关系满足<b>0.05的显著性水平</b>。</p>
      <br>
      <p>2.3方差分析</p>
      <br>
      <p>
        通过上面的相关性分析，可以初步得出地区与农村家庭的家庭总收入存在相关性，但是具体是不是不同地域的划分会显著的影响地域家庭的家庭收入，还需要通过<b>方差分析</b>来检测。将农村家庭的收入分为五个组，分别是东中部、西部、南部、北部。现在想要观察不同的分类变量是否会影响各地的工资收入水平。通过<b>单因素方差分析</b>来展开。
      </p>
      <br>
      <p>利用<b>python软件的statsmodels.formula.api模块</b>进行单因素方差分析。可以得到如下的结果表：</p>
      <br>
      <div style="margin-left:20%">
        <el-table :data="tableData" style="width: 60%">
          <el-table-column prop="date" label=" ">
          </el-table-column>
          <el-table-column prop="name" label="sum_sq">
          </el-table-column>
          <el-table-column prop="name2" label="df">
          </el-table-column>
          <el-table-column prop="name3" label="F">
          </el-table-column>
          <el-table-column prop="address" label="PR(>F)">
          </el-table-column>
        </el-table>
      </div>

      <br>
      <p align="center">表3-2单因素方差分析表</p>
      <br>
      <p>从上面的方差分析表可以得出，<b>F值分别为52.5和27.6</b>，都是满足在0.05的显著性水平下各组的均值不完全相等的，说明地域的不同会对中国农村家庭的收入带来显著性的影响差异。</p>
      <br>
    </div>
    <div class="title-7" id="title7" ref="title7">
      <h1 :class='{main_title7:true,xianshi3:sig7}'>结论与建议</h1>
      <h1 :class='{second_title7:true,xianshi3:sig7}'>展望未来，我们能做的还有很多......</h1>
    </div>
    <div class="zhengwen">

      <br>
      <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过上文的研究，统计描述性分析，可视化结果图以及农村地区和家庭收入水平之间的相关性以及显著性检验，提出几个实现乡村振兴的途径
      </p>
      <div style="display: flex; margin-bottom: 5vh;">
        <img class="img03" src="https://img1.imgtp.com/2022/02/12/nES138Ll.jpg" alt="">
        <div style="margin-top: 5vh;">
          <br>
          <p>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;城市的发展离不开农村的支持，实现乡村振兴一方面可以解决城乡发展不平衡问题。乡村振兴关系到了农业农村现代的实现、国家现代化的实现，可以从根本上解决现阶段我国农业不发达、农村不兴旺、农民不富裕的“三农”问题。让农村走上现代化的道路，提高农民的收入，缩小城乡收入。实施乡村振兴战略，是要从根本上解决目前我国农业不发达、农村不兴旺、农民不富裕的“三农”问题。通过牢固树立创新、协调、绿色、开放、共享“五大”发展理念，达到生产、生活、生态的“三生”协调，促进农业、加工业、现代服务业的“三业”融合发展，真正实现农业发展、农村变样、农民受惠，最终建成“看得见山、望得见水、记得住乡愁”、留得住人的美丽乡村、美丽中国。
          </p>
          <br>
        </div>
      </div>
      <p>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.要深入推进农业供给侧结构性改革，促进产业发展，加快建设现代农业产业体系、生产体系、经营体系，推动种植业、畜牧业、渔业、农产品加工业等转型升级，努力向现代农业迈进。找准产业，重点要基于更高效、更生态、更智慧的农业；其次应注重高附加值的农产品的生产和加工，延伸农业产业链，有针对性的要发挥农村资源优势，推进农业与新工业、互联网、旅游、养老等深度融合，建设现代农业公园等新业态，促进农村一二三产业融合发展，培育农业农村发展新动能，支持和鼓励农民参与建设现代农业产业。
        努力向现代农业迈进。</p>
      <br>
      <p>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.要在城乡融合发展制度设计、政策创新上想办法、求突破，缩小城乡差距，实现乡村振兴，既要发挥政府的主导作用、依靠农民自己勤奋劳动，更需要全社会的关心和支持。大家的参与和支持，是乡村建设的重要力量和重要资源。鼓励和引导社会资金和技术力量参与新农村建设，注重做好“三个相结合”，一是与农村综合改革和扶贫相结合，二是与提升新农村建设水平和加强农业农村环境整治相结合，三是与乡村经营管理相结合，吸引和集聚土地、资本、科技、人才、信息等现代要素，全面激活市场、激活要素、激活主体，形成农业农村经济发展新动力，让“产业兴旺、生态宜居、乡风文明、治理有效、生活富裕”逐步成为现实。加快农村公共设施建设，加快补齐农业农村发展短板，让农业强起来、农村美起来、农民富起来。让农村成为安居乐业的家园。
      </p>
      <br>
      <p>
        <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;要不忘初心，牢记使命，时刻保持思想信念的坚定，常怀一颗赤子之心，为了农业农村农民的发展积极贡献自己的力量，为缩小城乡差距，构建乡村振兴蓝图而不懈奋斗。</b>
      </p>
      <br>
    </div>
    <div class="jiewei">
      <div class="zhengwen" style="margin-left: 35%; margin-right: 20%; margin-top: 10vh;">
        <p>数据来源: 中国家庭追踪调查(CFPS)</p>
        <p>图片来源: 图片来源于网络</p>
        <p>学校：山东大学（威海）</p>
        <p>班级：数据科学与人工智能实验班</p>
        <p>团队成员: 范传进 许家路 赵依洋</p>
        <p>指导老师: 郭亮 王效强 王猛</p>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import '../../public/js/china.js'
  import '../../public/js/echarts-wordcloud.js'
  export default {
    created() {
      axios.get('http://82.156.173.187:8040/index').then(res => {
        this.fangwen = res.data.time
      })

    },
    mounted() {
      var myChart1 = this.$echarts.init(document.getElementById('main1'));
      myChart1.setOption({
        baseOption: {
          toolbox: {
            show: true,
            feature: {
              dataZoom: {
                yAxisIndex: 'none'
              },
              dataView: {
                readOnly: false
              },
              magicType: {
                type: ['line', 'bar']
              },
              restore: {},
              saveAsImage: {}
            }
          },
          timeline: {
            autoPlay: true,
            loop: true,
            data: ['2010', '2012', '2014', '2016', '2018']
          },
          tooltip: {},
          xAxis: {
            type: 'category',
            data: ['自来水', '井水', '江河湖水', '矿泉水', '窖水', '其他']
          },
          yAxis: {
            type: 'value',
            data: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
            max: 1.0
          },
          legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 0,
            bottom: 20,
            data: ['自来水', '井水', '江河湖水', '矿泉水', '窖水', '其他']
          },
          emphasis: {
            focus: 'series'
          },
          series: [{
              name: '农村',
              type: 'bar',
              showBackground: true,
              backgroundStyle: {
                color: 'rgba(180, 180, 180, 0.2)'
              },
            },
            {
              name: '城市',
              type: 'bar',
              showBackground: true,
            }, {
              name: '农村',
              type: 'pie',
              colcolorBy: 'data',
              radius: '30%',
              center: ['80%', '30%'],
            },
            {
              name: '城市',
              type: 'pie',
              colcolorBy: 'data',
              radius: '30%',
              center: ['55%', '30%'],
            },
          ]
        },
        options: [{
            title: {
              text: '2010家庭饮用水来源调查'
            },
            series: [{
              data: [0.391213933, 0.539251365, 0.013517026, 0.002209514, 0.037821679, 0.015986483]
            }, {
              data: [0.81894974, 0.170068985, 0.002393355, 0.006476137, 0.000563142, 0.001548641]
            }, {
              data: [{
                name: '自来水',
                value: 0.391213933
              }, {
                name: '井水',
                value: 0.539251365
              }, {
                name: '江河湖水',
                value: 0.013517026
              }, {
                name: '矿泉水',
                value: 0.002209514
              }, {
                name: '窖水',
                value: 0.037821679
              }, {
                name: '其他',
                value: 0.015986483
              }]
            }, {
              data: [{
                name: '自来水',
                value: 0.81894974
              }, {
                name: '井水',
                value: 0.170068985
              }, {
                name: '江河湖水',
                value: 0.002393355
              }, {
                name: '矿泉水',
                value: 0.006476137
              }, {
                name: '窖水',
                value: 0.000563142
              }, {
                name: '其他',
                value: 0.001548641
              }]
            }]
          },
          {
            title: {
              text: '2012家庭饮用水来源调查'
            },
            series: [{
              data: [0.47151277, 0.461268594, 0.009402189, 0.002104968, 0.031995509, 0.02371597]
            }, {
              data: [0.79553719, 0.176198347, 0.002809917, 0.012396694, 0.003305785, 0.009752066]
            }, {
              data: [{
                name: '自来水',
                value: 0.47151277
              }, {
                name: '井水',
                value: 0.461268594
              }, {
                name: '江河湖水',
                value: 0.009402189
              }, {
                name: '矿泉水',
                value: 0.002104968
              }, {
                name: '窖水',
                value: 0.031995509
              }, {
                name: '其他',
                value: 0.02371597
              }]
            }, {
              data: [{
                name: '自来水',
                value: 0.79553719
              }, {
                name: '井水',
                value: 0.176198347
              }, {
                name: '江河湖水',
                value: 0.002809917
              }, {
                name: '矿泉水',
                value: 0.012396694
              }, {
                name: '窖水',
                value: 0.003305785
              }, {
                name: '其他',
                value: 0.009752066
              }]
            }]
          },
          {
            title: {
              text: '2014家庭饮用水来源调查'
            },
            series: [{
              data: [0.519312695, 0.339818233, 0.007668276, 0.004970179, 0.03166714, 0.096563476]
            }, {
              data: [0.790690823, 0.137722787, 0.001472971, 0.011047282, 0.000589188, 0.058476948]
            }, {
              data: [{
                name: '自来水',
                value: 0.519312695
              }, {
                name: '井水',
                value: 0.339818233
              }, {
                name: '江河湖水',
                value: 0.007668276
              }, {
                name: '矿泉水',
                value: 0.004970179
              }, {
                name: '窖水',
                value: 0.03166714
              }, {
                name: '其他',
                value: 0.096563476
              }]
            }, {
              data: [{
                name: '自来水',
                value: 0.790690823
              }, {
                name: '井水',
                value: 0.137722787
              }, {
                name: '江河湖水',
                value: 0.001472971
              }, {
                name: '矿泉水',
                value: 0.011047282
              }, {
                name: '窖水',
                value: 0.000589188
              }, {
                name: '其他',
                value: 0.058476948
              }]
            }]
          },
          {
            title: {
              text: '2016家庭饮用水来源调查'
            },
            series: [{
              data: [0.607195518, 0.30507225, 0.006045414, 0.003981127, 0.019610734, 0.058094957]
            }, {
              data: [0.850224086, 0.109729652, 0.00216857, 0.019083418, 0.000722857, 0.018071418]
            }, {
              data: [{
                name: '自来水',
                value: 0.607195518
              }, {
                name: '井水',
                value: 0.30507225
              }, {
                name: '江河湖水',
                value: 0.006045414
              }, {
                name: '矿泉水',
                value: 0.003981127
              }, {
                name: '窖水',
                value: 0.019610734
              }, {
                name: '其他',
                value: 0.058094957
              }]
            }, {
              data: [{
                name: '自来水',
                value: 0.850224086
              }, {
                name: '井水',
                value: 0.109729652
              }, {
                name: '江河湖水',
                value: 0.00216857
              }, {
                name: '矿泉水',
                value: 0.019083418
              }, {
                name: '窖水',
                value: 0.000722857
              }, {
                name: '其他',
                value: 0.018071418
              }]
            }]
          },
          {
            title: {
              text: '2018家庭饮用水来源调查'
            },
            series: [{
              data: [0.634330569, 0.264958531, 0.005627962, 0.01214455, 0.013329384, 0.069609005]
            }, {
              data: [0.837151532, 0.100055203, 0.001794093, 0.040160088, 0.001242065, 0.019597019]
            }, {
              data: [{
                name: '自来水',
                value: 0.634330569
              }, {
                name: '井水',
                value: 0.264958531
              }, {
                name: '江河湖水',
                value: 0.005627962
              }, {
                name: '矿泉水',
                value: 0.01214455
              }, {
                name: '窖水',
                value: 0.013329384
              }, {
                name: '其他',
                value: 0.069609005
              }]
            }, {
              data: [{
                name: '自来水',
                value: 0.837151532
              }, {
                name: '井水',
                value: 0.100055203
              }, {
                name: '江河湖水',
                value: 0.001794093
              }, {
                name: '矿泉水',
                value: 0.040160088
              }, {
                name: '窖水',
                value: 0.001242065
              }, {
                name: '其他',
                value: 0.019597019
              }]
            }]
          },
        ]

      });

      var myChart2 = this.$echarts.init(document.getElementById('main2'));
      myChart2.setOption({
        baseOption: {
          toolbox: {
            show: true,
            feature: {
              dataZoom: {
                yAxisIndex: 'none'
              },
              dataView: {
                readOnly: false
              },
              magicType: {
                type: ['line', 'bar']
              },
              restore: {},
              saveAsImage: {}
            }
          },
          timeline: {
            autoPlay: true,
            loop: true,
            data: ['2010', '2012', '2014', '2016', '2018']
          },
          tooltip: {},
          grid: {
            x2: 100
          },
          yAxis: {
            type: 'category',
            data: ['北部农村', '南部农村', '北部城市', '南部城市']
          },
          xAxis: {
            type: 'value',
            data: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
          },
          legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 0,
            bottom: 20,
            data: ['自来水', '井水', '江河湖水', '矿泉水', '窖水', '其他']
          },
          emphasis: {
            focus: 'series'
          },
          series: [{
              name: '自来水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },
            {
              name: '井水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },

            {
              name: '江河湖水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },

            {
              name: '矿泉水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },

            {
              name: '窖水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },

            {
              name: '其他',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },
          ]
        },
        options: [{
            title: {
              text: '2010南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.386,
                0.399,
                0.800,
                0.837
              ]
            }, {
              data: [0.525,
                0.559,
                0.193,
                0.148
              ]
            }, {
              data: [0.012,
                0.015,
                0.001,
                0.003
              ]
            }, {
              data: [0.001,
                0.003,
                0.002,
                0.011
              ]
            }, {
              data: [0.057,
                0.010,
                0.001,
                0.000,
              ]
            }, {
              data: [0.018,
                0.013,
                0.002,
                0.001
              ]
            }]

          },

          {
            title: {
              text: '2012南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.451,
                0.503,
                0.790,
                0.801
              ]
            }, {
              data: [0.462,
                0.461,
                0.181,
                0.171
              ]
            }, {
              data: [0.006,
                0.014,
                0.001,
                0.005

              ]
            }, {
              data: [0.002,
                0.002,
                0.008,
                0.017

              ]
            }, {
              data: [0.052,
                0.002,
                0.007,
                0.000

              ]
            }, {
              data: [0.027,
                0.018,
                0.013,
                0.006
              ]
            }]
          },

          {
            title: {
              text: '2014南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.497,
                0.555,
                0.782,
                0.799

              ]
            }, {
              data: [0.377,
                0.281,
                0.163,
                0.112

              ]
            }, {
              data: [0.005,
                0.011,
                0.001,
                0.002

              ]
            }, {
              data: [0.004,
                0.007,
                0.009,
                0.013

              ]
            }, {
              data: [0.050,
                0.002,
                0.001,
                0.001

              ]
            }, {
              data: [0.067,
                0.144,
                0.044,
                0.073

              ]
            }]
          },
          {
            title: {
              text: '2016南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.603,
                0.615,
                0.865,
                0.836

              ]
            }, {
              data: [0.331,
                0.262,
                0.109,
                0.111

              ]
            }, {
              data: [0.004,
                0.010,
                0.001,
                0.003

              ]
            }, {
              data: [0.004,
                0.005,
                0.014,
                0.024

              ]
            }, {
              data: [0.032,
                0.000,
                0.001,
                0.000

              ]
            }, {
              data: [0.026,
                0.108,
                0.009,
                0.026

              ]
            }]
          },
          {
            title: {
              text: '2018南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.640,
                0.625,
                0.848,
                0.827,

              ]
            }, {
              data: [0.283,
                0.237,
                0.101,
                0.099

              ]
            }, {
              data: [0.005,
                0.006,
                0.001,
                0.003

              ]
            }, {
              data: [0.013,
                0.011,
                0.041,
                0.039

              ]
            }, {
              data: [0.020,
                0.002,
                0.002,
                0.000

              ]
            }, {
              data: [0.039,
                0.118,
                0.007,
                0.031

              ]
            }]
          },

        ]

      })


      var myChart3 = this.$echarts.init(document.getElementById('main3'));
      myChart3.setOption({
        baseOption: {
          toolbox: {
            show: true,
            feature: {
              dataZoom: {
                yAxisIndex: 'none'
              },
              dataView: {
                readOnly: false
              },
              magicType: {
                type: ['line', 'bar']
              },
              restore: {},
              saveAsImage: {}
            }
          },
          timeline: {
            autoPlay: true,
            loop: true,
            data: ['2010', '2012', '2014', '2016', '2018']
          },
          tooltip: {},
          grid: {
            x2: 100
          },
          yAxis: {
            type: 'category',
            data: ['东北部农村', '西部农村', '中部农村', '东部农村', '东北部城市', '西部城市', '中部城市', '东部城市']
          },
          xAxis: {
            type: 'value',
            data: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
          },
          legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 0,
            bottom: 20,
            data: ['自来水', '井水', '江河湖水', '矿泉水', '窖水', '其他']
          },
          emphasis: {
            focus: 'series'
          },
          series: [{
              name: '自来水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },
            {
              name: '井水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },

            {
              name: '江河湖水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },

            {
              name: '矿泉水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },

            {
              name: '窖水',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },

            {
              name: '其他',
              type: 'bar',
              showBackground: true,
              stack: 'total',
            },
          ]
        },
        options: [{
            title: {
              text: '2010南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.340,
                0.371,
                0.287,
                0.537,
                0.870,
                0.703,
                0.724,
                0.880

              ]
            }, {
              data: [0.651,
                0.479,
                0.671,
                0.450,
                0.125,
                0.291,
                0.263,
                0.103

              ]
            }, {
              data: [0.006,
                0.029,
                0.006,
                0.002,
                0.000,
                0.005,
                0.005,
                0.002

              ]
            }, {
              data: [0.000,
                0.004,
                0.001,
                0.002,
                0.000,
                0.000,
                0.005,
                0.013

              ]
            }, {
              data: [0.000,
                0.101,
                0.004,
                0.000,
                0.000,
                0.000,
                0.000,
                0.001

              ]
            }, {
              data: [0.002,
                0.015,
                0.030,
                0.008,
                0.003,
                0.001,
                0.003,
                0.000

              ]
            }]

          },

          {
            title: {
              text: '2012南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.444,
                0.480,
                0.339,
                0.597,
                0.847,
                0.674,
                0.748,
                0.849,

              ]
            }, {
              data: [0.546,
                0.375,
                0.629,
                0.377,
                0.138,
                0.306,
                0.217,
                0.117

              ]
            }, {
              data: [0.002,
                0.015,
                0.002,
                0.012,
                0.002,
                0.002,
                0.002,
                0.004

              ]
            }, {
              data: [0.002,
                0.002,
                0.001,
                0.003,
                0.004,
                0.004,
                0.010,
                0.022

              ]
            }, {
              data: [0.000,
                0.090,
                0.002,
                0.000,
                0.000,
                0.005,
                0.011,
                0.000

              ]
            }, {
              data: [0.006,
                0.037,
                0.027,
                0.011,
                0.009,
                0.009,
                0.012,
                0.008

              ]
            }]

          },
          {
            title: {
              text: '2014南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.468,
                0.537,
                0.425,
                0.603,
                0.871,
                0.714,
                0.708,
                0.837

              ]
            }, {
              data: [0.503,
                0.217,
                0.486,
                0.291,
                0.097,
                0.191,
                0.235,
                0.077

              ]
            }, {
              data: [0.001,
                0.016,
                0.002,
                0.005,
                0.000,
                0.001,
                0.003,
                0.001

              ]
            }, {
              data: [0.003,
                0.005,
                0.002,
                0.008,
                0.004,
                0.006,
                0.011,
                0.016

              ]
            }, {
              data: [0.000,
                0.082,
                0.013,
                0.000,
                0.000,
                0.002,
                0.001,
                0.000

              ]
            }, {
              data: [0.024,
                0.143,
                0.072,
                0.092,
                0.028,
                0.086,
                0.042,
                0.069

              ]
            }]

          },
          {
            title: {
              text: '2016南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.468,
                0.626,
                0.560,
                0.692,
                0.907,
                0.802,
                0.789,
                0.885

              ]
            }, {
              data: [0.524,
                0.213,
                0.380,
                0.256,
                0.075,
                0.157,
                0.180,
                0.062

              ]
            }, {
              data: [0.000,
                0.009,
                0.003,
                0.007,
                0.000,
                0.004,
                0.002,
                0.002

              ]
            }, {
              data: [0.005,
                0.002,
                0.008,
                0.002,
                0.010,
                0.017,
                0.015,
                0.026

              ]
            }, {
              data: [0.000,
                0.047,
                0.010,
                0.000,
                0.001,
                0.001,
                0.001,
                0.001

              ]
            }, {
              data: [0.002,
                0.102,
                0.038,
                0.043,
                0.007,
                0.019,
                0.013,
                0.024

              ]
            }]

          },
          {
            title: {
              text: '2018南北家庭饮用水来源调查'
            },
            series: [{
              data: [0.431,
                0.672,
                0.636,
                0.673,
                0.892,
                0.813,
                0.791,
                0.853

              ]
            }, {
              data: [0.552,
                0.175,
                0.279,
                0.244,
                0.067,
                0.147,
                0.158,
                0.059

              ]
            }, {
              data: [0.000,
                0.011,
                0.002,
                0.004,
                0.000,
                0.002,
                0.002,
                0.002

              ]
            }, {
              data: [0.015,
                0.010,
                0.014,
                0.012,
                0.035,
                0.017,
                0.031,
                0.059

              ]
            }, {
              data: [0.000,
                0.030,
                0.009,
                0.001,
                0.000,
                0.001,
                0.001,
                0.002

              ]
            }, {
              data: [0.002,
                0.102,
                0.060,
                0.065,
                0.005,
                0.019,
                0.017,
                0.025

              ]
            }]

          },
        ]

      })


      var myChart4 = this.$echarts.init(document.getElementById('main4'));
      myChart4.setOption({
        tooltip: {},
        visualMap: {
          max: 120000,
          inRange: {
            color: [
              '#313695',
              '#4575b4',
              '#74add1',
              '#abd9e9',
              '#e0f3f8',
              '#ffffbf',
              '#fee090',
              '#fdae61',
              '#f46d43',
              '#d73027',
              '#a50026'
            ]
          }
        },
        xAxis3D: {
          name: '年份',
          type: 'category',
          data: ['2010', '2012', '2014', '2016', '2018']
        },
        yAxis3D: {
          name: '地域',
          type: 'category',
          data: ['城市', '乡村']
        },
        zAxis3D: {
          name: '家庭收入',
          type: 'value'
        },
        grid3D: {
          boxWidth: 100,
          boxDepth: 40,
          viewControl: {
            // projection: 'orthographic'
          },
          light: {
            main: {
              intensity: 1.2,
              shadow: true
            },
            ambient: {
              intensity: 0.3
            }
          }
        },
        series: [{
          type: 'bar3D',
          data: [
            [0, 0, 21179.17],
            [0, 1, 36995.33],
            [1, 0, 37904.78],
            [1, 1, 56369.76],
            [2, 0, 42161.29],
            [2, 1, 69454.04],
            [3, 0, 57058.24],
            [3, 1, 94247.29],
            [4, 0, 60375.5],
            [4, 1, 117821.2]
          ],
          shading: 'lambert',
          label: {
            fontSize: 16,
            borderWidth: 1
          },

          emphasis: {
            label: {
              fontSize: 20,
              color: '#900'
            },
            itemStyle: {
              color: '#900'
            }
          }
        }]
      })

      var myChart5 = this.$echarts.init(document.getElementById('main5'));
      myChart5.setOption({
        tooltip: {},
        visualMap: {
          max: 50000,
          inRange: {
            color: [
              '#313695',
              '#4575b4',
              '#74add1',
              '#abd9e9',
              '#e0f3f8',
              '#ffffbf',
              '#fee090',
              '#fdae61',
              '#f46d43',
              '#d73027',
              '#a50026'
            ]
          }
        },
        xAxis3D: {
          name: '年份',
          type: 'category',
          data: ['2012', '2014', '2016', '2018']
        },
        yAxis3D: {
          name: '地域',
          type: 'category',
          data: ['城市', '乡村']
        },
        zAxis3D: {
          name: '家庭人均收入',
          type: 'value'
        },
        grid3D: {
          boxWidth: 100,
          boxDepth: 40,
          viewControl: {
            // projection: 'orthographic'
          },
          light: {
            main: {
              intensity: 1.2,
              shadow: true
            },
            ambient: {
              intensity: 0.3
            }
          }
        },
        series: [{
          type: 'bar3D',
          data: [
            [0, 0, 9516.024],
            [0, 1, 17898.59],
            [1, 0, 11390.78],
            [1, 1, 23929.07],
            [2, 0, 15814.65],
            [2, 1, 31928.3],
            [3, 0, 17763.31],
            [3, 1, 42001.07]
          ],
          shading: 'lambert',
          label: {
            fontSize: 16,
            borderWidth: 1
          },

          emphasis: {
            label: {
              fontSize: 20,
              color: '#900'
            },
            itemStyle: {
              color: '#900'
            }
          }
        }]
      })


      var myChart6 = this.$echarts.init(document.getElementById('main6'));
      myChart6.setOption({
          visualMap: {
            left: 'right',
            min: 0,
            max: 64183,
            inRange: {
              // prettier-ignore
              color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61',
                '#f46d43', '#d73027', '#a50026'
              ]
            },
            text: ['High', 'Low'],
            calculable: true
          },
          title: {
            text: '中国地图'
          },
          //提示框
          tooltip: {},
          series: [{
            id: 'economy',
            type: 'map',
            roam: true,
            map: 'china',
            itemStyle: {
              normal: {
                areaColor: 'rgb(5, 0, 27)',
                borderColor: 'rgb(6, 121, 252)',
                borderWidth: 2
              },
              emphasis: {
                areaColor: 'rgba(125,126,200,0.3)'
              },
              select: {
                areaColor: 'rgba(125,126,200,0.3)'
              }
            },
            label: {
              emphasis: {
                show: true,
                formatter: '{b}',
                color: 'rgb(255,255,255)',
                align: 'center'
              },
              select: {
                show: true,
                formatter: '{b}',
                color: 'rgb(255,255,255)',
                align: 'center'
              }
            },
            animationDurationUpdate: 3000,
            universalTransition: true,
            data: [{
                name: "南海诸岛",
                value: 0
              },
              {
                name: '北京',
                value: 62361
              },
              {
                name: '天津',
                value: 39506
              },
              {
                name: '上海',
                value: 64183
              },
              {
                name: '重庆',
                value: 26386
              },
              {
                name: '河北',
                value: 23446
              },
              {
                name: '河南',
                value: 21964
              },
              {
                name: '云南',
                value: 20084
              },
              {
                name: '辽宁',
                value: 29701
              },
              {
                name: '黑龙江',
                value: 22726
              },
              {
                name: '湖南',
                value: 25241
              },
              {
                name: '安徽',
                value: 23984
              },
              {
                name: '山东',
                value: 29205
              },
              {
                name: '新疆',
                value: 21500
              },
              {
                name: '江苏',
                value: 38096
              },
              {
                name: '浙江',
                value: 45840
              },
              {
                name: '江西',
                value: 24080
              },
              {
                name: '湖北',
                value: 25815
              },
              {
                name: '广西',
                value: 21485
              },
              {
                name: '甘肃',
                value: 17488
              },
              {
                name: '山西',
                value: 21990
              },
              {
                name: '内蒙古',
                value: 28376
              },
              {
                name: '陕西',
                value: 22528
              },
              {
                name: '吉林',
                value: 22798
              },
              {
                name: '福建',
                value: 32644
              },
              {
                name: '贵州',
                value: 18430
              },
              {
                name: '广东',
                value: 35810
              },
              {
                name: '青海',
                value: 20757
              },
              {
                name: '西藏',
                value: 17286
              },
              {
                name: '四川',
                value: 22461
              },
              {
                name: '宁夏',
                value: 22400
              },
              {
                name: '海南',
                value: 24579
              },
              {
                name: '台湾',
                value: 0
              },
              {
                name: '香港',
                value: 0
              },
              {
                name: '澳门',
                value: 0
              }
            ],
            roam: true,
          }],

        }

      )

      var myChart7 = this.$echarts.init(document.getElementById('main7'));
      myChart7.setOption({
        tooltip: {},
        visualMap: {
          max: 120000,
          inRange: {
            color: [
              '#313695',
              '#4575b4',
              '#74add1',
              '#abd9e9',
              '#e0f3f8',
              '#ffffbf',
              '#fee090',
              '#fdae61',
              '#f46d43',
              '#d73027',
              '#a50026'
            ]
          }
        },
        xAxis3D: {
          name: '年份',
          type: 'category',
          data: ['2010', '2012', '2014', '2016', '2018']
        },
        yAxis3D: {
          name: '地域',
          type: 'category',
          data: ['北部乡村', '南部乡村', '北部城市', '南部城市']
        },
        zAxis3D: {
          name: '家庭总收入',
          type: 'value'
        },
        grid3D: {
          boxWidth: 100,
          boxDepth: 40,
          viewControl: {
            // projection: 'orthographic'
          },
          light: {
            main: {
              intensity: 1.2,
              shadow: true
            },
            ambient: {
              intensity: 0.3
            }
          }
        },
        series: [{
          type: 'bar3D',
          data: [
            [0, 2, 28764],
            [0, 3, 44470],
            [0, 0, 17133],
            [0, 1, 26413],
            [1, 2, 47505],
            [1, 3, 65479],
            [1, 0, 36428],
            [1, 1, 40237],
            [2, 2, 51794],
            [2, 3, 87212],
            [2, 0, 38821],
            [2, 1, 45910],
            [3, 2, 76926],
            [3, 3, 110852],
            [3, 0, 44808],
            [3, 1, 77512],
            [4, 2, 91908],
            [4, 3, 142939],
            [4, 0, 53409],
            [4, 1, 70268]
          ],
          shading: 'lambert',
          label: {
            fontSize: 16,
            borderWidth: 1
          },

          emphasis: {
            label: {
              fontSize: 20,
              color: '#900'
            },
            itemStyle: {
              color: '#900'
            }
          }
        }]
      })

      var myChart8 = this.$echarts.init(document.getElementById('main8'));
      myChart8.setOption({
        tooltip: {},
        visualMap: {
          max: 120000,
          inRange: {
            color: [
              '#313695',
              '#4575b4',
              '#74add1',
              '#abd9e9',
              '#e0f3f8',
              '#ffffbf',
              '#fee090',
              '#fdae61',
              '#f46d43',
              '#d73027',
              '#a50026'
            ]
          }
        },
        xAxis3D: {
          name: '年份',
          type: 'category',
          data: ['2010', '2012', '2014', '2016', '2018']
        },
        yAxis3D: {
          name: '地域',
          type: 'category',
          data: ['东北部农村', '西部乡村', '中部乡村', '东部乡村', '东北部城市', '西部城市', '中部城市', '东部城市']
        },
        zAxis3D: {
          name: '家庭总收入',
          type: 'value'
        },
        grid3D: {
          boxWidth: 100,
          boxDepth: 40,
          viewControl: {
            // projection: 'orthographic'
          },
          light: {
            main: {
              intensity: 1.2,
              shadow: true
            },
            ambient: {
              intensity: 0.3
            }
          }
        },
        series: [{
          type: 'bar3D',
          data: [
            [0, 0, 19077],
            [0, 1, 14759],
            [0, 2, 19505],
            [0, 3, 32282],
            [0, 4, 28514],
            [0, 5, 29284],
            [0, 6, 31719],
            [0, 7, 46419],
            [1, 0, 33057],
            [1, 1, 34403],
            [1, 2, 41995],
            [1, 3, 40744],
            [1, 4, 43652],
            [1, 5, 48099],
            [1, 6, 51624],
            [1, 7, 68985],
            [2, 0, 37936],
            [2, 1, 34017],
            [2, 2, 44169],
            [2, 3, 49042],
            [2, 4, 49700],
            [2, 5, 46759],
            [2, 6, 57476],
            [2, 7, 95659],
            [3, 0, 40524],
            [3, 1, 48260],
            [3, 2, 53486],
            [3, 3, 81277],
            [3, 4, 67390],
            [3, 5, 68575],
            [3, 6, 96474],
            [3, 7, 116405],
            [4, 0, 51541],
            [4, 1, 53119],
            [4, 2, 61809],
            [4, 3, 71242],
            [4, 4, 87243],
            [4, 5, 98330],
            [4, 6, 98788],
            [4, 7, 149569]
          ],
          shading: 'lambert',
          label: {
            fontSize: 16,
            borderWidth: 1
          },

          emphasis: {
            label: {
              fontSize: 20,
              color: '#900'
            },
            itemStyle: {
              color: '#900'
            }
          }
        }]
      })

      var myChart9 = this.$echarts.init(document.getElementById('main9'));
      myChart9.setOption({
        legend: {},
        tooltip: {
          trigger: 'axis',
          showContent: false
        },
        dataset: {
          source: [
            ['year', '2010', '2012', '2014', '2016', '2018'],
            ['政府部门/党政机关/人民团体', 0.051115619, 0.029961927, 0.045495905, 0.044166667, 0.050274941],
            ['事业单位', 0.055578093, 0.034762457, 0.020018198, 0.0125, 0.022780833],
            ['国有企业', 0.054361055, 0.051481543, 0.070973612, 0.049166667, 0.051846033],
            ['私营企业/个体工商户', 0.642190669, 0.668266843, 0.589626934, 0.605833333, 0.630793401],
            ['外商/港澳台商企业', 0.034482759, 0.028803178, 0.020928116, 0.031666667, 0.033354281],
            ['个人/家庭', 0.074239351, 0.117199139, 0.204731574, 0.215, 0.187957581],
            ['民办非企业组织/协会/行会/基金会/村居委会', 0.042190669, 0.033603708, 0.028207461, 0.014166667, 0.017282011],
            ['其他', 0.045841785, 0.035921205, 0.020018198, 0.0275, 0.005710919]
          ]
        },
        xAxis: {
          type: 'category'
        },
        yAxis: {
          gridIndex: 0
        },
        grid: {
          top: '55%'
        },
        series: [{
            type: 'line',
            smooth: true,
            seriesLayoutBy: 'row',
            emphasis: {
              focus: 'series'
            }
          },
          {
            type: 'line',
            smooth: true,
            seriesLayoutBy: 'row',
            emphasis: {
              focus: 'series'
            }
          },
          {
            type: 'line',
            smooth: true,
            seriesLayoutBy: 'row',
            emphasis: {
              focus: 'series'
            }
          },
          {
            type: 'line',
            smooth: true,
            seriesLayoutBy: 'row',
            emphasis: {
              focus: 'series'
            }
          },
          {
            type: 'line',
            smooth: true,
            seriesLayoutBy: 'row',
            emphasis: {
              focus: 'series'
            }
          },
          {
            type: 'line',
            smooth: true,
            seriesLayoutBy: 'row',
            emphasis: {
              focus: 'series'
            }
          },
          {
            type: 'line',
            smooth: true,
            seriesLayoutBy: 'row',
            emphasis: {
              focus: 'series'
            }
          },
          {
            type: 'line',
            smooth: true,
            seriesLayoutBy: 'row',
            emphasis: {
              focus: 'series'
            }
          },
          {
            type: 'pie',
            id: 'pie',
            radius: '30%',
            center: ['50%', '35%'],
            emphasis: {
              focus: 'self'
            },

          }
        ]
      })

      var myChart10 = this.$echarts.init(document.getElementById('main10'));
      myChart10.setOption({
        tooltip: {},
        visualMap: {
          max: 1,
          inRange: {
            color: [
              '#313695',
              '#4575b4',
              '#74add1',
              '#abd9e9',
              '#e0f3f8',
              '#ffffbf',
              '#fee090',
              '#fdae61',
              '#f46d43',
              '#d73027',
              '#a50026'
            ]
          }
        },
        xAxis3D: {
          name: '工作',
          type: 'category',
          data: ['政府部门/党政机关/人民团体', '事业单位', '国有企业', '私营企业/个体工商户', '外商/港澳台商企业', '个人/家庭', '其他']
        },
        yAxis3D: {
          name: '地域',
          type: 'category',
          data: ['北部乡村', '南部乡村', '北部城市', '南部城市']
        },
        zAxis3D: {
          name: '工作差异',
          type: 'value'
        },
        grid3D: {
          boxWidth: 100,
          boxDepth: 40,
          viewControl: {
            // projection: 'orthographic'
          },
          light: {
            main: {
              intensity: 1.2,
              shadow: true
            },
            ambient: {
              intensity: 0.3
            }
          }
        },
        series: [{
          type: 'bar3D',
          data: [
            [0, 0, 0.050397878],
            [0, 1, 0.050096339],
            [0, 2, 0.034653465],
            [0, 3, 0.047520661],
            [1, 0, 0.023872679],
            [1, 1, 0.021194605],
            [1, 2, 0.027227723],
            [1, 3, 0.030991736],
            [2, 0, 0.054376658],
            [2, 1, 0.048169557],
            [2, 2, 0.091584158],
            [2, 3, 0.059917355],
            [3, 0, 0.656498674],
            [3, 1, 0.59344894],
            [3, 2, 0.702970297],
            [3, 3, 0.685950413],
            [4, 0, 0.01193634],
            [4, 1, 0.015414258],
            [4, 2, 0.012376238],
            [4, 3, 0.047520661],
            [5, 0, 0.173740053],
            [5, 1, 0.233140655],
            [5, 2, 0.002475248],
            [5, 3, 0.082644628],
            [6, 0, 0.029177719],
            [6, 1, 0.038535645],
            [6, 2, 0.128712871],
            [6, 3, 0.045454545]
          ],
          shading: 'lambert',
          label: {
            fontSize: 16,
            borderWidth: 1
          },

          emphasis: {
            label: {
              fontSize: 20,
              color: '#900'
            },
            itemStyle: {
              color: '#900'
            }
          }
        }]
      })

      var myChart11 = this.$echarts.init(document.getElementById('main11'));
      myChart11.setOption({
        tooltip: {},
        visualMap: {
          max: 1,
          inRange: {
            color: [
              '#313695',
              '#4575b4',
              '#74add1',
              '#abd9e9',
              '#e0f3f8',
              '#ffffbf',
              '#fee090',
              '#fdae61',
              '#f46d43',
              '#d73027',
              '#a50026'
            ]
          }
        },
        xAxis3D: {
          name: '工作',
          type: 'category',
          data: ['政府部门/党政机关/人民团体', '事业单位', '国有企业', '私营企业/个体工商户', '外商/港澳台商企业', '个人/家庭', '其他']
        },
        yAxis3D: {
          name: '地域',
          type: 'category',
          data: ['东北部农村', '西部农村', '中部农村', '东部农村', '东北部城市', '西部城市', '中部城市', '东部城市']
        },
        zAxis3D: {
          name: '工作差异',
          type: 'value'
        },
        grid3D: {
          boxWidth: 100,
          boxDepth: 100,
          viewControl: {
            // projection: 'orthographic'
          },
          light: {
            main: {
              intensity: 1.2,
              shadow: true
            },
            ambient: {
              intensity: 0.3
            }
          }
        },
        series: [{
          type: 'bar3D',
          data: [
            [0, 0, 0.073770492],
            [0, 1, 0.068762279],
            [0, 2, 0.0125],
            [0, 3, 0.049689441],
            [0, 4, 0.036697248],
            [0, 5, 0.074257426],
            [0, 6, 0.00921659],
            [0, 7, 0.044444444],
            [1, 0, 0.040983607],
            [1, 1, 0.009823183],
            [1, 2, 0.0125],
            [1, 3, 0.046583851],
            [1, 4, 0.018348624],
            [1, 5, 0.024752475],
            [1, 6, 0.013824885],
            [1, 7, 0.044444444],
            [2, 0, 0.049180328],
            [2, 1, 0.053045187],
            [2, 2, 0.053125],
            [2, 3, 0.049689441],
            [2, 4, 0.110091743],
            [2, 5, 0.069306931],
            [2, 6, 0.046082949],
            [2, 7, 0.083333333],
            [3, 0, 0.631147541],
            [3, 1, 0.626719057],
            [3, 2, 0.646875],
            [3, 3, 0.621118012],
            [3, 4, 0.71559633],
            [3, 5, 0.707920792],
            [3, 6, 0.695852535],
            [3, 7, 0.677777778],
            [4, 0, 0.016393443],
            [4, 1, 0.009823183],
            [4, 2, 0.025],
            [4, 3, 0.00621118],
            [4, 4, 0.009174312],
            [4, 5, 0.012352],
            [4, 6, 0.023041475],
            [4, 7, 0.061111111],
            [5, 0, 0.172131148],
            [5, 1, 0.188605108],
            [5, 2, 0.23125],
            [5, 3, 0.189440994],
            [5, 4, 0.091743119],
            [5, 5, 0.099009901],
            [5, 6, 0.138248848],
            [5, 7, 0.058333333],
            [6, 0, 0.016393443],
            [6, 1, 0.043222004],
            [6, 2, 0.01875],
            [6, 3, 0.037267081],
            [6, 4, 0.018348624],
            [6, 5, 0.012400475],
            [6, 6, 0.073732719],
            [6, 7, 0.030555556]
          ],
          shading: 'lambert',
          label: {
            fontSize: 16,
            borderWidth: 1
          },

          emphasis: {
            label: {
              fontSize: 20,
              color: '#900'
            },
            itemStyle: {
              color: '#900'
            }
          }
        }]
      })

      var myChart12 = this.$echarts.init(document.getElementById('main12'));
      myChart12.setOption({
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          left: 'center',
          top: 'bottom',
          data: [
            '文盲/半文盲',
            '小学',
            '初中',
            '高中/中专/技校/职高',
            '大专',
            '大学本科',
            '硕士',
            '博士'
          ]
        },
        toolbox: {
          show: true,
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            dataView: {
              readOnly: false
            },
            restore: {},
            saveAsImage: {}
          }
        },
        series: [{
            name: '农村',
            type: 'pie',
            radius: [20, 140],
            center: ['25%', '50%'],
            roseType: 'radius',
            itemStyle: {
              borderRadius: 5
            },
            label: {
              show: false
            },
            emphasis: {
              label: {
                show: true
              }
            },
            data: [{
                value: 0.037127072,
                name: '大学本科'
              },
              {
                value: 0.312375691,
                name: '初中'
              },
              {
                value: 0.261546961,
                name: '小学'
              },
              {
                value: 0.192265193,
                name: '文盲/半文盲'
              },


              {
                value: 0.134254144,
                name: '高中/中专/技校/职高'
              },
              {
                value: 0.059226519,
                name: '大专'
              },

              {
                value: 0.002762431,
                name: '硕士'
              },
              {
                value: 0.000331492,
                name: '博士'
              }
            ]
          },
          {
            name: '城市',
            type: 'pie',
            radius: [20, 140],
            center: ['75%', '50%'],
            roseType: 'radius',
            itemStyle: {
              borderRadius: 5
            },
            label: {
              show: false
            },
            emphasis: {
              label: {
                show: true
              }
            },
            data: [{
                value: 0.277210702,
                name: '初中'
              },
              {
                value: 0.194262383,
                name: '高中/中专/技校/职高'
              },

              {
                value: 0.151176534,
                name: '小学'
              },


              {
                value: 0.141936177,
                name: '大专'
              },
              {
                value: 0.136993661,
                name: '大学本科'
              },
              {
                value: 0.084130225,
                name: '文盲/半文盲'
              },
              {
                value: 0.012571183,
                name: '硕士'
              },
              {
                value: 0.001396798,
                name: '博士'
              }
            ]
          }
        ]
      })

      var myChart13 = this.$echarts.init(document.getElementById('main13'));
      myChart13.setOption({
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            // Use axis to trigger tooltip
            type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
          }
        },
        legend: {},
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value',
        },
        yAxis: {
          type: 'category',
          data: ['北部农村', '南部农村', '北部城市', '南部城市']
        },
        series: [{
            name: '文盲/半文盲',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.235136583, 0.162151994, 0.101666315, 0.06595092]
          },
          {
            name: '小学',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.263256561, 0.260346125, 0.157983548, 0.144171779]
          },
          {
            name: '初中',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.274772362, 0.338976674, 0.268719679, 0.286152498]
          },
          {
            name: '高中/中专/技校/职高',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.130958757, 0.136568849, 0.190044294, 0.198729185]
          },
          {
            name: '大专',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.057846813, 0.060195636, 0.137734655, 0.14636284]
          },
          {
            name: '大学本科',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.03561864, 0.038186606, 0.131617802, 0.143295355]
          }, {
            name: '硕士',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.001310283, 0.002009782, 0.009546298, 0.013680105]
          }, {
            name: '博士',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0, 0.000554333, 0.001587407, 0.00105552]
          },

        ]
      })

      var myChart14 = this.$echarts.init(document.getElementById('main14'));
      myChart14.setOption({
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            // Use axis to trigger tooltip
            type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
          }
        },
        legend: {},
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value',
        },
        yAxis: {
          type: 'category',
          data: ['东北部农村', '西部农村', '中部农村', '东部农村', '东北部城市', '西部城市', '中部城市', '东部城市']
        },
        series: [{
            name: '文盲/半文盲',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.135429262, 0.263064883, 0.128557875, 0.146239554, 0.063520871, 0.128078818, 0.069788384,
              0.072513996

            ]
          },
          {
            name: '小学',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.252720677, 0.26937642, 0.277039848, 0.235376045, 0.137023593, 0.178683386, 0.157136425,
              0.135430552

            ]
          },
          {
            name: '初中',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.400241838, 0.259530422, 0.345351044, 0.34354689, 0.289473684, 0.286162114, 0.281404773,
              0.265795788

            ]
          },
          {
            name: '高中/中专/技校/职高',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.095525998, 0.125473365, 0.151328273, 0.148560817, 0.200544465, 0.170622481, 0.199459703,
              0.203412423

            ]
          },
          {
            name: '大专',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.061668682, 0.0472103, 0.061195446, 0.078458682, 0.16061706, 0.111957009, 0.144529491,
              0.152759264

            ]
          },
          {
            name: '大学本科',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.052204353, 0.032072456, 0.033629981, 0.039854225, 0.134208711, 0.113643977, 0.135425034,
              0.150159691

            ]
          }, {
            name: '硕士',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0.00120919, 0.002019692, 0.001897533, 0.005571031, 0.012704174, 0.008956561, 0.010355696,
              0.015995734

            ]
          }, {
            name: '博士',
            type: 'bar',
            stack: 'total',
            emphasis: {
              focus: 'series'
            },
            data: [0, 0.000252461, 0, 0.000928505, 0.000907441, 0.000895656, 0.000900495, 0.002132765

            ]
          },

        ]
      })

      var myChart15 = this.$echarts.init(document.getElementById('main15'));
      myChart15.setOption({
        series: [{
          type: 'wordCloud',
          shape: 'circle',
          left: 'center',
          top: 'center',
          right: null,
          bottom: null,
          width: '70%',
          height: '80%',
          sizeRange: [12, 60],
          rotationRange: [-90, 90],
          rotationStep: 45,
          gridSize: 8,
          drawOutOfBound: false,
          textStyle: {
            normal: {
              color: function () {
                // Random color
                return 'rgb(' + [
                  Math.round(Math.random() * 160),
                  Math.round(Math.random() * 160),
                  Math.round(Math.random() * 160)
                ].join(',') + ')';
              }
            },
            emphasis: {
              focus: 'self',

              textStyle: {
                textShadowBlur: 10,
                textShadowColor: '#333'
              }
            },
          },
          data: [{
              name: '基因编辑',
              value: 1228
            },
            {
              name: '婴儿',
              value: 981
            },
            {
              name: '贺建奎',
              value: 363
            }, {
              "name": "花鸟市场",
              "value": 1446
            },
            {
              "name": "汽车",
              "value": 928
            },
            {
              "name": "视频",
              "value": 906
            },
            {
              "name": "电视",
              "value": 825
            },
            {
              "name": "Lover Boy 88",
              "value": 514
            },
            {
              "name": "动漫",
              "value": 486
            },
            {
              "name": "音乐",
              "value": 59
            },
            {
              "name": "直播",
              "value": 163
            },
            {
              "name": "广播电台",
              "value": 86
            },
            {
              "name": "戏曲曲艺",
              "value": 17
            },
            {
              "name": "演出票务",
              "value": 6
            },
            {
              "name": "给陌生的你听",
              "value": 1
            },
            {
              "name": "资讯",
              "value": 1437
            },
            {
              "name": "商业财经",
              "value": 422
            },
            {
              "name": "娱乐八卦",
              "value": 353
            },
            {
              "name": "军事",
              "value": 331
            },
            {
              "name": "科技资讯",
              "value": 313
            },
            {
              "name": "社会时政",
              "value": 307
            },
            {
              "name": "时尚",
              "value": 43
            },
            {
              "name": "网络奇闻",
              "value": 15
            },
            {
              "name": "旅游出行",
              "value": 438
            },
            {
              "name": "景点类型",
              "value": 957
            },
            {
              "name": "国内游",
              "value": 927
            },
            {
              "name": "远途出行方式",
              "value": 908
            },
            {
              "name": "酒店",
              "value": 693
            },
            {
              "name": "关注景点",
              "value": 611
            },
            {
              "name": "旅游网站偏好",
              "value": 512
            },
            {
              "name": "出国游",
              "value": 382
            },
            {
              "name": "交通票务",
              "value": 312
            },
            {
              "name": "旅游方式",
              "value": 187
            },
            {
              "name": "旅游主题",
              "value": 163
            },
            {
              "name": "港澳台",
              "value": 104
            },
            {
              "name": "本地周边游",
              "value": 3
            },
            {
              "name": "小卖家",
              "value": 1331
            },
            {
              "name": "全日制学校",
              "value": 941
            },
            {
              "name": "基础教育科目",
              "value": 585
            },
            {
              "name": "考试培训",
              "value": 473
            },
            {
              "name": "语言学习",
              "value": 358
            },
            {
              "name": "留学",
              "value": 246
            },
            {
              "name": "K12课程培训",
              "value": 207
            },
            {
              "name": "艺术培训",
              "value": 194
            },
            {
              "name": "技能培训",
              "value": 104
            },
            {
              "name": "IT培训",
              "value": 87
            },
            {
              "name": "高等教育专业",
              "value": 63
            },
            {
              "name": "家教",
              "value": 48
            },
          ]
        }]
      })



      window.addEventListener('scroll', this.jianting)
    },
    beforeDestroy() {
    window.removeEventListener('scroll', this.jianting)
  },
    data() {
      return {
        activeIndex: '1',
        sig2: false,
        sig3: false,
        sig4: false,
        sig5: false,
        sig6: false,
        sig7: false,
        fangwen: 0,
        tableData: [{
          date: 'spearman相关系数',
          name: '-0.02348',
          address: '-0.042785'
        }, {
          date: 'P_value',
          name: '0.09618',
          address: '0.002429'
        }],
        tableData2: [{
          date: 'C(N_S)',
          name: '1.16E+12',
          name2: '1',
          name3: '52.493218',
          address: '4.97E-13'
        }, {
          date: 'C(E_C_W)',
          name: '1.22E+12',
          name2: '2',
          name3: '27.610798',
          address: '1.19E-12'
        }, {
          date: 'Residual',
          name: '1.11E+14',
          name2: '5016',
          name3: 'NaN',
          address: 'NaN'
        }, ],
        option: 'map'
      }
    },

    methods: {
          reload() {
this.$router.go(0)
    },
      tiaozhuan() {
        this.$router.push('/login');
      },
      qiehuan() {
        var data = [{
            name: "南海诸岛",
            value: 0
          },
          {
            name: '北京',
            value: 62361
          },
          {
            name: '天津',
            value: 39506
          },
          {
            name: '上海',
            value: 64183
          },
          {
            name: '重庆',
            value: 26386
          },
          {
            name: '河北',
            value: 23446
          },
          {
            name: '河南',
            value: 21964
          },
          {
            name: '云南',
            value: 20084
          },
          {
            name: '辽宁',
            value: 29701
          },
          {
            name: '黑龙江',
            value: 22726
          },
          {
            name: '湖南',
            value: 25241
          },
          {
            name: '安徽',
            value: 23984
          },
          {
            name: '山东',
            value: 29205
          },
          {
            name: '新疆',
            value: 21500
          },
          {
            name: '江苏',
            value: 38096
          },
          {
            name: '浙江',
            value: 45840
          },
          {
            name: '江西',
            value: 24080
          },
          {
            name: '湖北',
            value: 25815
          },
          {
            name: '广西',
            value: 21485
          },
          {
            name: '甘肃',
            value: 17488
          },
          {
            name: '山西',
            value: 21990
          },
          {
            name: '内蒙古',
            value: 28376
          },
          {
            name: '陕西',
            value: 22528
          },
          {
            name: '吉林',
            value: 22798
          },
          {
            name: '福建',
            value: 32644
          },
          {
            name: '贵州',
            value: 18430
          },
          {
            name: '广东',
            value: 35810
          },
          {
            name: '青海',
            value: 20757
          },
          {
            name: '西藏',
            value: 17286
          },
          {
            name: '四川',
            value: 22461
          },
          {
            name: '宁夏',
            value: 22400
          },
          {
            name: '海南',
            value: 24579
          },
          {
            name: '台湾',
            value: 0
          },
          {
            name: '香港',
            value: 0
          },
          {
            name: '澳门',
            value: 0
          }
        ]
        var myChart6 = this.$echarts.init(document.getElementById('main6'));
        if (this.option == 'map') {
          this.option = 'bar'
          myChart6.setOption({
            tooltip: {},
            xAxis: {
              type: 'value'
            },
            yAxis: {
              type: 'category',
              axisLabel: {
                rotate: 30
              },
              data: data.map(function (item) {
                return item.name;
              })
            },
            animationDurationUpdate: 3000,
            series: {
              type: 'bar',
              id: 'economy',
              data: data.map(function (item) {
                return item.value;
              }),
              universalTransition: true
            }
          }, true);
        } else {
          this.option = 'map'
          myChart6.setOption({
            visualMap: {
              left: 'right',
              min: 0,
              max: 64183,
              inRange: {
                // prettier-ignore
                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61',
                  '#f46d43', '#d73027', '#a50026'
                ]
              },
              text: ['High', 'Low'],
              calculable: true
            },
            title: {
              text: '中国地图'
            },
            //提示框
            tooltip: {},
            series: [{
              id: 'economy',
              type: 'map',
              roam: true,
              map: 'china',
              itemStyle: {
                normal: {
                  areaColor: 'rgb(5, 0, 27)',
                  borderColor: 'rgb(6, 121, 252)',
                  borderWidth: 2
                },
                emphasis: {
                  areaColor: 'rgba(125,126,200,0.3)'
                },
                select: {
                  areaColor: 'rgba(125,126,200,0.3)'
                }
              },
              label: {
                emphasis: {
                  show: true,
                  formatter: '{b}',
                  color: 'rgb(255,255,255)',
                  align: 'center'
                },
                select: {
                  show: true,
                  formatter: '{b}',
                  color: 'rgb(255,255,255)',
                  align: 'center'
                }
              },
              animationDurationUpdate: 3000,
              universalTransition: true,
              data: [{
                  name: "南海诸岛",
                  value: 0
                },
                {
                  name: '北京',
                  value: 62361
                },
                {
                  name: '天津',
                  value: 39506
                },
                {
                  name: '上海',
                  value: 64183
                },
                {
                  name: '重庆',
                  value: 26386
                },
                {
                  name: '河北',
                  value: 23446
                },
                {
                  name: '河南',
                  value: 21964
                },
                {
                  name: '云南',
                  value: 20084
                },
                {
                  name: '辽宁',
                  value: 29701
                },
                {
                  name: '黑龙江',
                  value: 22726
                },
                {
                  name: '湖南',
                  value: 25241
                },
                {
                  name: '安徽',
                  value: 23984
                },
                {
                  name: '山东',
                  value: 29205
                },
                {
                  name: '新疆',
                  value: 21500
                },
                {
                  name: '江苏',
                  value: 38096
                },
                {
                  name: '浙江',
                  value: 45840
                },
                {
                  name: '江西',
                  value: 24080
                },
                {
                  name: '湖北',
                  value: 25815
                },
                {
                  name: '广西',
                  value: 21485
                },
                {
                  name: '甘肃',
                  value: 17488
                },
                {
                  name: '山西',
                  value: 21990
                },
                {
                  name: '内蒙古',
                  value: 28376
                },
                {
                  name: '陕西',
                  value: 22528
                },
                {
                  name: '吉林',
                  value: 22798
                },
                {
                  name: '福建',
                  value: 32644
                },
                {
                  name: '贵州',
                  value: 18430
                },
                {
                  name: '广东',
                  value: 35810
                },
                {
                  name: '青海',
                  value: 20757
                },
                {
                  name: '西藏',
                  value: 17286
                },
                {
                  name: '四川',
                  value: 22461
                },
                {
                  name: '宁夏',
                  value: 22400
                },
                {
                  name: '海南',
                  value: 24579
                },
                {
                  name: '台湾',
                  value: 0
                },
                {
                  name: '香港',
                  value: 0
                },
                {
                  name: '澳门',
                  value: 0
                }
              ],
              roam: true,
            }],

          }, true);
        }

      },
      jianting() {
        if (this.$refs.title2.getBoundingClientRect().top < 300) {
          this.sig2 = true
        }
        if (this.$refs.title3.getBoundingClientRect().top < 300) {
          this.sig3 = true
        }
        if (this.$refs.title4.getBoundingClientRect().top < 300) {
          this.sig4 = true
        }
        if (this.$refs.title5.getBoundingClientRect().top < 300) {
          this.sig5 = true
        }
        if (this.$refs.title6.getBoundingClientRect().top < 300) {
          this.sig6 = true
        }
        if (this.$refs.title7.getBoundingClientRect().top < 300) {
          this.sig7 = true
        }

      },
    }
  }
</script>

<style>
  html,
  body {
    border: 0;
    margin: 0;
    /* display: flex;
    justify-items: center;
    margin: 0 auto; */
    scroll-behavior: smooth;
  }

  h2,
  h3,
  h4 {
    text-shadow: 1px 1px grey;
  }

  .mulubutton {
    width: 10%;
    background-color: rgba(122, 193, 235, 0.884);
    border: 0;
  }

  .mulubutton1 {
    width: 10%;
    background-color: rgba(122, 193, 235, 0.884);
    border: 0;
  }

  .title {
    width: 100%;
    height: 100vh;
    float: right;
    background-image: url(https://img1.imgtp.com/2022/02/12/9YweXC3z.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: center center;
  }

  .title-2 {
    width: 100%;
    height: 80vh;
    background-image: url(https://img1.imgtp.com/2022/02/12/V3gIj79V.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: center center;
  }

  .title-3 {
    width: 100%;
    height: 80vh;
    background-image: url(https://img1.imgtp.com/2022/02/12/cQerfK9e.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: center center;
  }

  .title-4 {
    width: 100%;
    height: 80vh;
    background-image: url(https://img1.imgtp.com/2022/02/12/wdcy8LEh.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: center center;
  }

  .title-5 {
    width: 100%;
    height: 80vh;
    background-image: url(https://img1.imgtp.com/2022/02/12/BEQF1uoq.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: center center;
  }

  .title-6 {
    width: 100%;
    height: 80vh;
    background-image: url(https://img1.imgtp.com/2022/02/12/D41xkX7N.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: center center;
  }

  .title-7 {
    width: 100%;
    height: 80vh;
    background-image: url(https://img1.imgtp.com/2022/02/12/nUm0n1TA.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: center center;
  }

  .img01 {
    margin-top: 5vh;
    margin-right: 5%;
    height: 60vh;
    width: 45%;
  }

  .img03 {
    margin-top: 5vh;
    margin-right: 5%;
    height: 60vh;
    width: 50%;
  }

  .img02 {
    margin-top: 5vh;
    margin-left: 5%;
    height: 50vh;
    width: 50%;
  }


  .mulu {
    background-color: rgba(255, 255, 255, 0.6);
    margin-top: 0;
    display: none;
  }

  @media (min-width:320px) and (max-width:480px) {
    .loginbu{
      margin-left:20% !important
    }
    .img01 {
      display: none;
    }

    .img02 {
      display: none;
    }

    .img03 {
      display: none;
    }

    .charts {
      width: 100%;
      height: 100vh;
    }

    .charts_ditu {
      width: 100%;
      height: 120vh;
    }

    #main1 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main2 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main3 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main4 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main5 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main6 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main7 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main8 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main9 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main10 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main11 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main12 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main13 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main14 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main15 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    .mulu {
      float: left;
      position: fixed;
      left: 60%;
      font-size: smaller;
    }

    .mulubutton {
      float: left;
      position: fixed;
      left: 60%;
      font-size: smaller;
    }

    .mulubutton1 {
      float: left;
      position: fixed;
      left: 60%;
      font-size: smaller;
    }

    .fangwen {
      color: #fff;
      margin-top: 5vh;
      margin-left: 70%;
      font-size: 8px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }


    .table>tbody>tr>td,
    .table>tbody>tr>th,
    .table>tfoot>tr>td,
    .table>tfoot>tr>th,
    .table>thead>tr>td,
    .table>thead>tr>th {
      margin: 4px !important;
    }

    .xiyulu {
      width: 80%;
      margin-top: 5vh;
      margin-left: 15%;
      margin-right: 20%;
      font-size: 18px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .zhuxi {
      margin-left: 55%;
      font-size: 18px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .img {
      width: 100%;
      margin-top: 5vh;
      height: 20vh;
    }

    .tuchu {
      font-size: 25px;
    }

    .zhengwen {
      margin-left: 20%;
      margin-right: 20%;
      color: black;
      font-size: 18px;
      font-weight: 200;
    }

    .main_title {
      color: #fff;
      margin-top: 20vh;
      margin-left: 10%;
      font-size: 25px;
      font-weight: 800;
      animation: show;
      animation-duration: 5s
    }

    .second_title {
      color: #fff;
      margin-top: 5vh;
      margin-left: 22%;
      font-size: 20px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .main_title2 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 25px;
      font-weight: 800;
      position: absolute;
    }

    .second_title2 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 20px;
      font-weight: 600;
      position: absolute;
    }

    .main_title3 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 25px;
      font-weight: 800;
      position: absolute;
    }

    .second_title3 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 20px;
      font-weight: 600;
      position: absolute;
    }

    .main_title4 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 25px;
      font-weight: 800;
      position: absolute;
    }

    .second_title4 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 20px;
      font-weight: 600;
      position: absolute;
    }

    .main_title5 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 25px;
      font-weight: 800;
      position: absolute;
    }

    .second_title5 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 20px;
      font-weight: 600;
      position: absolute;
    }

    .main_title6 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 25px;
      font-weight: 800;
      position: absolute;
    }

    .second_title6 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 20px;
      font-weight: 600;
      position: absolute;
    }

    .main_title7 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 25px;
      font-weight: 800;
      position: absolute;
    }

    .second_title7 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 25%;
      font-size: 20px;
      font-weight: 600;
      position: absolute;
    }
  }

  @media (min-width:480px) and (max-width:640px) {
    .loginbu{
      margin-left:20% !important
    }
    .img01 {
      display: none;
    }

    .img02 {
      display: none;
    }

    .img03 {
      display: none;
    }

    .charts {
      width: 100%;
      height: 100vh;
    }

    .charts_ditu {
      width: 100%;
      height: 120vh;
    }

    #main1 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main2 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main3 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main4 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main5 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main6 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main7 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main8 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main9 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main10 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main11 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main12 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main13 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main14 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main15 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    .mulu {
      float: left;
      position: fixed;
      left: 60%;
      font-size: small;
    }

    .mulubutton {
      float: left;
      position: fixed;
      left: 60%;
      font-size: small;
    }

    .mulubutton1 {
      float: left;
      position: fixed;
      left: 60%;
      font-size: small;
    }

    .fangwen {
      color: #fff;
      margin-top: 5vh;
      margin-left: 80%;
      font-size: 10px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .table {
      width: 20%;
      height: 50vh;
      display: flex;
      place-items: center;
      font-size: 15px;
    }

    .table>tbody>tr>td,
    .table>tbody>tr>th,
    .table>tfoot>tr>td,
    .table>tfoot>tr>th,
    .table>thead>tr>td,
    .table>thead>tr>th {
      margin: 5px !important;
    }

    .xiyulu {
      width: 80%;
      margin-top: 5vh;
      margin-left: 15%;
      margin-right: 20%;
      font-size: 22px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .zhuxi {
      margin-left: 5%;
      font-size: 22px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .img {
      width: 100%;
      margin-top: 5vh;
      height: 20vh;
    }

    .tuchu {
      font-size: 30px;
    }

    .zhengwen {
      margin-left: 20%;
      margin-right: 20%;
      color: black;
      font-size: 22px;
      font-weight: 200;
    }

    .main_title {
      color: #fff;
      margin-top: 20vh;
      margin-left: 10%;
      font-size: 35px;
      font-weight: 800;
      animation: show;
      animation-duration: 5s
    }

    .second_title {
      color: #fff;
      margin-top: 5vh;
      margin-left: 22%;
      font-size: 30px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .main_title2 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 35px;
      font-weight: 800;
      position: absolute;
    }

    .second_title2 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 30px;
      font-weight: 600;
      position: absolute;
    }

    .main_title3 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 35px;
      font-weight: 800;
      position: absolute;
    }

    .second_title3 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 30px;
      font-weight: 600;
      position: absolute;
    }

    .main_title4 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 35px;
      font-weight: 800;
      position: absolute;
    }

    .second_title4 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 30px;
      font-weight: 600;
      position: absolute;
    }

    .main_title5 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 35px;
      font-weight: 800;
      position: absolute;
    }

    .second_title5 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 30px;
      font-weight: 600;
      position: absolute;
    }

    .main_title6 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 35px;
      font-weight: 800;
      position: absolute;
    }

    .second_title6 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 30px;
      font-weight: 600;
      position: absolute;
    }

    .main_title7 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 35px;
      font-weight: 800;
      position: absolute;
    }

    .second_title7 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 25%;
      font-size: 30px;
      font-weight: 600;
      position: absolute;
    }
  }

  @media (min-width:640px) and (max-width:900px) {
    .loginbu{
      margin-left:25% !important
    }
    .img01 {
      display: none;
    }

    .img02 {
      display: none;
    }

    .img03 {
      display: none;
    }

    .charts {
      width: 100%;
      height: 100vh;
    }

    .charts_ditu {
      width: 100%;
      height: 120vh;
    }

    #main1 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main2 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main3 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main4 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main5 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main6 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main7 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main8 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main9 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main10 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main11 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main12 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main13 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main14 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    #main15 {
      margin: 0 auto;
      width: 100%;
      height: 100vh;
      display: flex;
      place-items: center;
    }

    .mulu {
      float: left;
      position: fixed;
      left: 60%;
      font-size: medium;
    }

    .mulubutton {
      float: left;
      position: fixed;
      left: 60%;
      font-size: medium;
    }

    .mulubutton1 {
      float: left;
      position: fixed;
      left: 60%;
      font-size: medium;
    }

    .table {
      width: 30%;
      height: 50vh;
      display: flex;
      place-items: center;
      font-size: 20px;
    }

    .table>tbody>tr>td,
    .table>tbody>tr>th,
    .table>tfoot>tr>td,
    .table>tfoot>tr>th,
    .table>thead>tr>td,
    .table>thead>tr>th {
      margin: 6px !important;
    }

    .xiyulu {
      width: 80%;
      margin-top: 5vh;
      margin-left: 15%;
      margin-right: 20%;
      font-size: 25px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .zhuxi {
      margin-left: 55%;
      font-size: 25px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .img {
      width: 100%;
      margin-top: 5vh;
      height: 20vh;
    }

    .tuchu {
      font-size: 33px;
    }

    .zhengwen {
      margin-left: 20%;
      margin-right: 20%;
      color: black;
      font-size: 25px;
      font-weight: 200;
    }

    .main_title {
      color: #fff;
      margin-top: 20vh;
      margin-left: 10%;
      font-size: 45px;
      font-weight: 800;
      animation: show;
      animation-duration: 5s
    }

    .second_title {
      color: #fff;
      margin-top: 5vh;
      margin-left: 22%;
      font-size: 40px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .fangwen {
      color: #fff;
      margin-top: 5vh;
      margin-left: 80%;
      font-size: 20px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .main_title2 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 45px;
      font-weight: 800;
      position: absolute;
    }

    .second_title2 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 40px;
      font-weight: 600;
      position: absolute;
    }

    .main_title3 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 45px;
      font-weight: 800;
      position: absolute;
    }

    .second_title3 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 40px;
      font-weight: 600;
      position: absolute;
    }

    .main_title4 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 45px;
      font-weight: 800;
      position: absolute;
    }

    .second_title4 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 40px;
      font-weight: 600;
      position: absolute;
    }

    .main_title5 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 45px;
      font-weight: 800;
      position: absolute;
    }

    .second_title5 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 40px;
      font-weight: 600;
      position: absolute;
    }

    .main_title6 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 45px;
      font-weight: 800;
      position: absolute;
    }

    .second_title6 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 40px;
      font-weight: 600;
      position: absolute;
    }

    .main_title7 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 45px;
      font-weight: 800;
      position: absolute;
    }

    .second_title7 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 25%;
      font-size: 40px;
      font-weight: 600;
      position: absolute;
    }
  }

  @media (min-width:900px) and (max-width:1350px) {
        .loginbu{
      margin-left:30% !important
    }
    .img01 {
      display: none;
    }

    .img02 {
      display: none;
    }

    .img03 {
      display: none;
    }

    .charts {
      width: 100%;
      height: 50vh;
    }

    .charts_ditu {
      width: 100%;
      height: 80vh;
    }

    #main1 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main2 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main3 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main4 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main5 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main6 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main7 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main8 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main9 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main10 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main11 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main12 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main13 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main14 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main15 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    .mulu {
      float: left;
      position: fixed;
      left: 70%;
      font-size: medium;
    }

    .mulubutton {
      float: left;
      position: fixed;
      left: 70%;
      font-size: medium;
    }

    .mulubutton1 {
      float: left;
      position: fixed;
      left: 70%;
      font-size: medium;
    }

    .table {
      width: 30%;
      height: 50vh;
      display: flex;
      place-items: center;
      font-size: 30px;
    }

    .table>tbody>tr>td,
    .table>tbody>tr>th,
    .table>tfoot>tr>td,
    .table>tfoot>tr>th,
    .table>thead>tr>td,
    .table>thead>tr>th {
      margin: 7px !important;
    }

    .xiyulu {
      width: 80%;
      margin-top: 5vh;
      margin-left: 15%;
      margin-right: 20%;
      font-size: 27px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .zhuxi {
      margin-left: 55%;
      font-size: 27px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .img {
      width: 100%;
      margin-top: 5vh;
      height: 20vh;
    }

    .tuchu {
      font-size: 35px;
    }

    .zhengwen {
      margin-left: 20%;
      margin-right: 20%;
      color: black;
      font-size: 27px;
      font-weight: 200;
    }

    .main_title {
      color: #fff;
      margin-top: 20vh;
      margin-left: 10%;
      font-size: 55px;
      font-weight: 800;
      animation: show;
      animation-duration: 5s
    }

    .second_title {
      color: #fff;
      margin-top: 5vh;
      margin-left: 22%;
      font-size: 50px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .fangwen {
      color: #fff;
      margin-top: 5vh;
      margin-left: 75%;
      font-size: 30px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .main_title2 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 55px;
      font-weight: 800;
      position: absolute;
    }

    .second_title2 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 50px;
      font-weight: 600;
      position: absolute;
    }

    .main_title3 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 55px;
      font-weight: 800;
      position: absolute;
    }

    .second_title3 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 50px;
      font-weight: 600;
      position: absolute;
    }

    .main_title4 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 55px;
      font-weight: 800;
      position: absolute;
    }

    .second_title4 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 50px;
      font-weight: 600;
      position: absolute;
    }

    .main_title5 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 55px;
      font-weight: 800;
      position: absolute;
    }

    .second_title5 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 50px;
      font-weight: 600;
      position: absolute;
    }

    .main_title6 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 55px;
      font-weight: 800;
      position: absolute;
    }

    .second_title6 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 22%;
      font-size: 50px;
      font-weight: 600;
      position: absolute;
    }

    .main_title7 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 55px;
      font-weight: 800;
      position: absolute;
    }

    .second_title7 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 35%;
      font-size: 50px;
      font-weight: 600;
      position: absolute;
    }
  }

  @media (min-width:1350px) {
    .loginbu{
      margin-left:80% !important
    }
    .charts {
      width: 100%;
      height: 50vh;
    }

    .charts_ditu {
      width: 100%;
      height: 80vh;
    }

    #main1 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main2 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main3 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main4 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main5 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main6 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main7 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main8 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main9 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main10 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main11 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main12 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main13 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main14 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    #main15 {
      margin: 0 auto;
      width: 50%;
      height: 50vh;
      display: flex;
      place-items: center;
    }

    .mulu {
      float: left;
      position: fixed;
      left: 80%;
      font-size: large;
    }

    .mulubutton {
      float: left;
      position: fixed;
      left: 85%;
      font-size: large;
    }

    .mulubutton1 {
      float: left;
      position: fixed;
      left: 85%;
      font-size: large;
    }

    .xiyulu {
      width: 80%;
      margin-top: 5vh;
      margin-left: 15%;
      margin-right: 20%;
      font-size: 32px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .zhuxi {
      margin-left: 55%;
      font-size: 32px;
      color: #8B0000;
      font-weight: bold;
      text-shadow: rgba(0, 0, 0, 0.4) 0px 4px 5px;
    }

    .img {
      width: 100%;
      margin-top: 5vh;
      height: 20vh;
    }

    .tuchu {
      font-size: 28px;
    }

    .zhengwen {
      margin-left: 20%;
      margin-right: 20%;
      color: black;
      font-size: 20px;
      font-weight: 200;
    }

    .main_title {
      color: #fff;
      margin-top: 20vh;
      margin-left: 10%;
      font-size: 100px;
      font-weight: 800;
      animation: show;
      animation-duration: 5s
    }

    .second_title {
      color: #fff;
      margin-top: 5vh;
      margin-left: 42%;
      font-size: 60px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .fangwen {
      color: #fff;
      margin-top: 5vh;
      margin-left: 70%;
      font-size: 40px;
      font-weight: 600;
      animation: show;
      animation-duration: 5s
    }

    .main_title2 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 100px;
      font-weight: 800;
      position: absolute;
    }

    .second_title2 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 42%;
      font-size: 60px;
      font-weight: 600;
      position: absolute;
    }

    .main_title3 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 100px;
      font-weight: 800;
      position: absolute;
    }

    .second_title3 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 42%;
      font-size: 60px;
      font-weight: 600;
      position: absolute;
    }

    .main_title4 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 100px;
      font-weight: 800;
      position: absolute;
    }

    .second_title4 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 42%;
      font-size: 60px;
      font-weight: 600;
      position: absolute;
    }

    .main_title5 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 100px;
      font-weight: 800;
      position: absolute;
    }

    .second_title5 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 42%;
      font-size: 60px;
      font-weight: 600;
      position: absolute;
    }

    .main_title6 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 100px;
      font-weight: 800;
      position: absolute;
    }

    .second_title6 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 42%;
      font-size: 60px;
      font-weight: 600;
      position: absolute;
    }

    .main_title7 {
      color: #fff;
      display: none;
      margin-top: 30vh;
      margin-left: 10%;
      font-size: 100px;
      font-weight: 800;
      position: absolute;
    }

    .second_title7 {
      color: #fff;
      display: none;
      margin-top: 50vh;
      margin-left: 35%;
      font-size: 60px;
      font-weight: 600;
      position: absolute;
    }
  }

  .xianshi3 {
    display: inline;
    animation: show;
    animation-duration: 4s
  }

  @keyframes show {
    0% {
      opacity: 0;
    }

    25% {
      opacity: 0;
    }

    100% {
      opacity: 1;
    }
  }



  .changebutton {
    margin-left: 25%;
    height: 5vh;
    width: 25%;
    background-color: rgba(122, 193, 235, 0.884);
    border: 0;
  }



  .xiaoshi {
    display: none !important;
  }

  .jiewei {
    display: flex;
    background-image: url('https://img1.imgtp.com/2022/02/12/v5JbY5gk.png');
    background-size: cover;
    background-position: center center;
  }
</style>
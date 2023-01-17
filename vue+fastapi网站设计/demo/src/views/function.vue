<template>
  <div class="bg">
    <div class="yetou">
      <div class="tuichubu">
        <el-button type="danger" @click="tuichu"><i class="el-icon-download" style="transform:rotate(90deg);"></i>退出登录
        </el-button>
      </div>
    </div>
    <el-tabs :tab-position="tabPosition">
      <el-tab-pane>
        <span slot="label"><i class="el-icon-s-promotion"></i> 连接显示数据库</span>
        <el-button type="primary" :loading=jiazai @click="lianjie()">连接数据库</el-button>
        <div  class="s1">
          <div class="biaodan" v-show="xianshibu==true">表单名称</div>
          <el-select v-model="value" placeholder="请选择" v-show="xianshibu==true">
            <el-option-group v-for="group in options" :key="group.label" :label="group.label">
              <el-option v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-option-group>
          </el-select>
          <div class="s2">
            <el-button type="primary" plain v-show="xianshibu==true" @click="huoqu()">获取数据</el-button>
          </div>
        </div>

        <el-table :data="tableData2" stripe height="70vh" style="width: 100%;" v-show="xianshibu==true">
          <el-table-column v-for="item in labelname" :key="item.key" :prop="item.name" :label="item.name">
          </el-table-column>

        </el-table>
        <div  v-show="xianshibu==true">
          <el-tag class="s3"><i class="el-icon-s-order"></i>总条数：{{tiaoshu1}}</el-tag>
          <el-tag class="s4" type="warning"><i
              class="el-icon-s-management"></i>总页数：{{yeshu1}}</el-tag>
          <el-tag  class="s5" type="success"><i class="el-icon-edit"></i>当前页数：{{yeshu2}}
          </el-tag>
        </div>
        <div class="s9" v-show="xianshibu==true">
          <el-button class="s6" type="primary" icon="el-icon-arrow-left" @click="qianyi">上一页</el-button>
          <el-input class="s7" v-model="yeshu3" placeholder="请输入页数" ></el-input>
          <el-button  type="primary" icon="el-icon-search" @click="tiaozhuan">跳转</el-button>
          <el-button  class="s8" type="primary" @click="houyi">下一页<i
              class="el-icon-arrow-right el-icon--right"></i></el-button>

        </div>


      </el-tab-pane>


      <el-tab-pane>
        <span slot="label"><i class="el-icon-s-claim"></i> 增删查改</span>
        <el-table :data="tableData" style="width: 100%">
          <el-table-column prop="order" label="命令" width='800'>
          </el-table-column>
          <el-table-column prop="status" label="状态" width='200'>
          </el-table-column>

        </el-table>
        <el-input type="textarea" autosize placeholder="请输入命令" v-model="textarea1"
          style="margin-top:5vh;width:70%;margin-left:12%;">
        </el-input>
        <div style="margin-left:40%;margin-top:5vh">
          <el-tooltip class="item" effect="dark" content="若创建新表，新表的最后一个字必须为汉字！" placement="top-start">
            <el-button type="primary" plain @click="zeng()" :loading=jiazai2>发送命令</el-button>
          </el-tooltip>
        </div>
        <el-table :data="tableData3" stripe height="70vh" style="width: 100%;" v-show="xianshi2==true">
          <el-table-column v-for="item in labelname2" :key="item.key" :prop="item.name" :label="item.name">
          </el-table-column>

        </el-table>
        <div v-show="xianshi2==true">
          <el-tag class="s3"><i class="el-icon-s-order"></i>总条数：{{tiaoshu12}}</el-tag>
          <el-tag class="s4" type="warning"><i
              class="el-icon-s-management"></i>总页数：{{yeshu12}}</el-tag>
          <el-tag class="s5" type="success"><i
              class="el-icon-edit"></i>当前页数：{{yeshu22}}</el-tag>
        </div>
        <div class="s9" v-show="xianshi2==true">
          <el-button type="primary" icon="el-icon-arrow-left" class="s6" @click="qianyi2">上一页</el-button>
          <el-input v-model="yeshu32" placeholder="请输入页数" class="s7"></el-input>
          <el-button type="primary" icon="el-icon-search" @click="tiaozhuan2">跳转</el-button>
          <el-button type="primary" class="s8" @click="houyi2">下一页<i
              class="el-icon-arrow-right el-icon--right"></i></el-button>

        </div>

      </el-tab-pane>

      <el-tab-pane label="echarts可视化">
        <span slot="label"><i class="el-icon-camera-solid"></i> echarts可视化</span>
        <el-form :inline="true" :model="formInline" class="demo-form-inline" style="margin-top:5vh">
          <el-form-item label="数据范围">
            <el-select v-model="formInline.diqu" placeholder="数据范围">
              <el-option label="南北部对比" value="1"></el-option>
              <el-option label="东中西部对比" value="2"></el-option>
            </el-select>
          </el-form-item>

          <el-form-item label="是否多年对比">
            <el-select v-model="formInline.duibi" placeholder="是否多年对比">
              <el-option label="是" value="1"></el-option>
              <el-option label="否" value="2"></el-option>
            </el-select>
          </el-form-item>
          <div style="display:flex">
            <div style="margin-top:1vh;margin-right:2%;margin-left:2%">图表1名称</div>
            <el-select v-model="tubiaovalue1" placeholder="请选择">
              <el-option-group v-for="group in options" :key="group.label" :label="group.label">
                <el-option v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-option-group>
            </el-select>

            <div style="margin-top:1vh;margin-right:2%;margin-left:2%">图表1字段</div>
            <el-select v-model="biaoqianvalue1" placeholder="请选择">
              <el-option-group v-for="group in options2" :key="group.label" :label="group.label">
                <el-option v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-option-group>
            </el-select>
          </div>
          <div style="display:flex">
            <div style="margin-top:5vh;margin-right:2%;margin-left:2%" v-show="formInline.duibi==1&tubiaovalue1!= '' ">
              图表2名称</div>
            <el-select v-model="tubiaovalue2" placeholder="请选择" v-show="formInline.duibi==1&tubiaovalue1!= '' "
              style="margin-top:4vh;">
              <el-option-group v-for="group in options" :key="group.label" :label="group.label">
                <el-option v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-option-group>
            </el-select>

            <div style="margin-top:5vh;margin-right:2%;margin-left:2%" v-show="formInline.duibi==1&tubiaovalue1!= '' ">
              图表2字段</div>
            <el-select v-model="biaoqianvalue2" placeholder="请选择" v-show="formInline.duibi==1&tubiaovalue1!= '' "
              style="margin-top:4vh;">
              <el-option-group v-for="group in options3" :key="group.label" :label="group.label">
                <el-option v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-option-group>
            </el-select>
          </div>
          <div style="display:flex">
            <div style="margin-top:5vh;margin-right:2%;margin-left:2%" v-show="formInline.duibi==1&tubiaovalue2!= '' ">
              图表3名称</div>
            <el-select v-model="tubiaovalue3" placeholder="请选择" v-show="formInline.duibi==1&tubiaovalue2!= '' "
              style="margin-top:4vh;">
              <el-option-group v-for="group in options" :key="group.label" :label="group.label">
                <el-option v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-option-group>
            </el-select>

            <div style="margin-top:5vh;margin-right:2%;margin-left:2%" v-show="formInline.duibi==1&tubiaovalue2!= '' ">
              图表3字段</div>
            <el-select v-model="biaoqianvalue3" placeholder="请选择" v-show="formInline.duibi==1&tubiaovalue2!= '' "
              style="margin-top:4vh;">
              <el-option-group v-for="group in options4" :key="group.label" :label="group.label">
                <el-option v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-option-group>
            </el-select>
          </div>


          <div style="display:flex" v-if="chuxian==true">
            <div style="margin-top:5vh;margin-right:2%;margin-left:2%">图表类型</div>
            <el-select v-model="tubiaoleixing" placeholder="请选择" style="margin-top:4vh;margin-right:2%;margin-left:2%"
              v-if="chuxian1==true">
              <el-option v-for="item in options5" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <el-select v-model="tubiaoleixing" placeholder="请选择" style="margin-top:4vh;margin-right:2%;margin-left:2%"
              v-if="chuxian2==true">
              <el-option v-for="item in options6" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <el-select v-model="tubiaoleixing" placeholder="请选择" style="margin-top:4vh;margin-right:2%;margin-left:2%"
              v-if="chuxian3==true">
              <el-option v-for="item in options7" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <el-select v-model="tubiaoleixing" placeholder="请选择" style="margin-top:4vh;margin-right:2%;margin-left:2%"
              v-if="chuxian4==true">
              <el-option v-for="item in options8" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <el-select v-model="tubiaoleixing" placeholder="请选择" style="margin-top:4vh;margin-right:2%;margin-left:2%"
              v-if="chuxian5==true">
              <el-option v-for="item in options9" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
            <el-select v-model="tubiaoleixing" placeholder="请选择" style="margin-top:4vh;margin-right:2%;margin-left:2%"
              v-if="chuxian6==true">
              <el-option v-for="item in options10" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>



          <el-form-item>
            <el-tooltip class="item" effect="dark" content="获取字段名，前请先连接数据库" placement="top-start">
              <el-button type="primary" @click="gain" style="margin-top:4vh;">获取字段名</el-button>
            </el-tooltip>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="over" style="margin-top:4vh;margin-left:5%">清空</el-button>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit" style="margin-top:4vh;margin-left:5%">查询数据</el-button>
          </el-form-item>
          <el-form-item>
            <el-tooltip class="item" effect="dark" content="请勿选取同一表中多列数据进行画图" placement="top-start">
              <el-button type="primary" @click="draw" style="margin-top:4vh;margin-left:5%">绘制图表</el-button>
            </el-tooltip>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="tishi" style="margin-top:4vh;;margin-left:5%">操作步骤</el-button>
          </el-form-item>
        </el-form>
        <div style="display:flex">
          <div style="width: 40%;">
            <el-table :data="tableData4" height="60vh">
              <el-table-column v-for="item in labelname3" :key="item.key" :prop="item.key" :label="item.name">
              </el-table-column>

            </el-table>
            <div >
              <el-tag class="s3"><i class="el-icon-s-order"></i>总条数：{{tiaoshu13}}
              </el-tag>
              <el-tag class="s4" type="warning"><i
                  class="el-icon-s-management"></i>总页数：{{yeshu13}}</el-tag>
              <el-tag class="s5" type="success"><i
                  class="el-icon-edit"></i>当前页数：{{yeshu23}}</el-tag>
            </div>
            <div class="s9">
              <el-button type="primary" icon="el-icon-arrow-left" class="s6" @click="qianyi3">上一页
              </el-button>
              <el-input v-model="yeshu33" placeholder="请输入页数" class="s7"></el-input>
              <el-button type="primary" icon="el-icon-search" @click="tiaozhuan3" style="margin-left:2%;">跳转</el-button>
              <el-button type="primary" class="s8" @click="houyi3">下一页<i
                  class="el-icon-arrow-right el-icon--right"></i></el-button>

            </div>

          </div>
          <div id="main" style="width:60%">
          </div>
        </div>

      </el-tab-pane>
      <el-tab-pane>
        <span slot="label"><i class="el-icon-s-custom"></i> 关于我们</span>
        <div style="display:flex">
          <div class="img"></div>
          <div class="wenzi3">
            <div>我们是来自山东大学（威海）2020级数据科学与人工智能实验班的成员，本可视化平台是山东大学（威海）2020级数据科学与人工智能实验班大作业的其中一项内容。
            </div>
            <div>
              在之前的工作中，我们利用中国家庭追踪调查（CFPS）数据，设计了数据库架构和关系。并且进行了从南北、东中西进行数据分析，撰写了一篇关于中国城乡差异和如何乡村振兴的分析报告。在这一部分工作中，我们开发了一个可视化平台，该平台具有连接显示数据库、数据操作、数据可视化等功能。
              以下为三阶段成果及原理讲解的B站视频链接。</div>
          </div>
        </div>
        <div style="display:flex;width:100%;height:40vh">
          <div class="fengmian" onclick="window.open('https://www.bilibili.com/video/BV1YF411h758/')"></div>
          <div class="fengmian2" onclick="window.open('https://www.bilibili.com/video/BV1Qi4y1R7WF/')"></div>
          <div class="fengmian3" onclick="window.open('https://www.bilibili.com/video/BV1tq4y187n6/')"></div>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
  import axios from 'axios';




  export default {
    created() {
      if (this.$session.get('signal') != 1) {
        this.$router.push('/');
      }
      axios.get('http://82.156.173.187:8040/get_records', {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + this.$session.get('token')
        }
      }).then(res => {
        var i
        for (i = 0; i < 10; i++) {
          if (res.data.records[i] != null) {
            var tip = {
              order: res.data.records[i],
              status: 'success'
            }
            this.tableData.push(tip)
          }

        }
      })
      this.$message({
        message: "尊敬的" + this.$session.get('username') + ",你好！",
        type: 'success'
      });

    },

    methods: {
      tishi() {
        this.$notify({
          title: '提示',
          message: '操作步骤：选择数据范围、是否多年对比、数据表名称 → 获取字段名 → 选择绘图字段 → 查询数据 → 选择图表类型 → 绘制图表',
          duration: 0
        });
      },
      qianyi3() {
        if (this.yeshu23 == 1) {
          this.$message({
            message: '前面没有了，向后看看吧',
            type: 'warning'
          });
        } else {
          this.yeshu23 = this.yeshu23 - 1;
          axios.post('http://82.156.173.187:8040/page3', {
            page: this.yeshu23,
            tip: this.shuqian
          }, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + this.$session.get('token')
            }
          }).then(res => {
            var i

            this.tableData4 = []
            var tip5 = {}
            var tip6 = {}
            var tip7 = {}
            this.tubiaoleixing = ''
            if (this.tubiaovalue2 == '') {
              for (i = 0; i < res.data.biaoqian1.data.length; i++) {
                tip5 = {
                  'a': res.data.biaoqian1.data[i]
                }
                this.tableData4.push(tip5)
              }
            }

            if (this.tubiaovalue2 != '' & this.tubiaovalue3 == '') {
              for (i = 0; i < res.data.biaoqian2.data.length; i++) {
                tip6 = {
                  'a': res.data.biaoqian1.data[i],
                  'b': res.data.biaoqian2.data[i]
                }
                this.tableData4.push(tip6)
              }
            }




            if (this.tubiaovalue3 != '') {
              for (i = 0; i < res.data.biaoqian1.data.length; i++) {
                tip7 = {
                  'a': res.data.biaoqian1.data[i],
                  'b': res.data.biaoqian2.data[i],
                  'c': res.data.biaoqian3.data[i]
                }
                this.tableData4.push(tip7)
              }
            }

          })

        }

      },
      houyi3() {
        if (this.yeshu23 == this.yeshu13) {
          this.$message({
            message: '后面没有了，向前看看吧',
            type: 'warning'
          });
        } else {
          this.yeshu23 = this.yeshu23 + 1;
          axios.post('http://82.156.173.187:8040/page3', {
            page: this.yeshu23,
            tip: this.shuqian
          }, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + this.$session.get('token')
            }
          }).then(res => {
            var i
            this.tableData4 = []
            var tip5 = {}
            var tip6 = {}
            var tip7 = {}
            this.tubiaoleixing = ''
            if (this.tubiaovalue2 == '') {
              for (i = 0; i < res.data.biaoqian1.data.length; i++) {
                tip5 = {
                  'a': res.data.biaoqian1.data[i]
                }
                this.tableData4.push(tip5)
              }
            }

            if (this.tubiaovalue2 != '' & this.tubiaovalue3 == '') {
              for (i = 0; i < res.data.biaoqian2.data.length; i++) {
                tip6 = {
                  'a': res.data.biaoqian1.data[i],
                  'b': res.data.biaoqian2.data[i]
                }
                this.tableData4.push(tip6)
              }
            }




            if (this.tubiaovalue3 != '') {
              for (i = 0; i < res.data.biaoqian1.data.length; i++) {
                tip7 = {
                  'a': res.data.biaoqian1.data[i],
                  'b': res.data.biaoqian2.data[i],
                  'c': res.data.biaoqian3.data[i]
                }
                this.tableData4.push(tip7)
              }
            }

          })

        }

      },
      tiaozhuan3() {
        if (this.yeshu33 < 1) {
          this.$message({
            message: '无法到达指定页数，请重新输入',
            type: 'warning'
          });
        } else {
          if (this.yeshu33 > this.yeshu13) {
            this.$message({
              message: '无法到达指定页数，请重新输入',
              type: 'warning'
            });
          } else {
            this.yeshu23 = Number(this.yeshu33);
            axios.post('http://82.156.173.187:8040/page3', {
              page: this.yeshu33,
              tip: this.shuqian
            }, {
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + this.$session.get('token')
              }
            }).then(res => {
              var i
              this.tableData4 = []
              var tip5 = {}
              var tip6 = {}
              var tip7 = {}
              this.tubiaoleixing = ''
              if (this.tubiaovalue2 == '') {
                for (i = 0; i < res.data.biaoqian1.data.length; i++) {
                  tip5 = {
                    'a': res.data.biaoqian1.data[i]
                  }
                  this.tableData4.push(tip5)
                }
              }

              if (this.tubiaovalue2 != '' & this.tubiaovalue3 == '') {
                for (i = 0; i < res.data.biaoqian2.data.length; i++) {
                  tip6 = {
                    'a': res.data.biaoqian1.data[i],
                    'b': res.data.biaoqian2.data[i]
                  }
                  this.tableData4.push(tip6)
                }
              }




              if (this.tubiaovalue3 != '') {
                for (i = 0; i < res.data.biaoqian1.data.length; i++) {
                  tip7 = {
                    'a': res.data.biaoqian1.data[i],
                    'b': res.data.biaoqian2.data[i],
                    'c': res.data.biaoqian3.data[i]
                  }
                  this.tableData4.push(tip7)
                }
              }

            })

          }
        }

      },
      qianyi2() {
        if (this.yeshu22 == 1) {
          this.$message({
            message: '前面没有了，向后看看吧',
            type: 'warning'
          });
        } else {
          this.yeshu22 = this.yeshu22 - 1;
          axios.post('http://82.156.173.187:8040/page2', {
            page: this.yeshu22,
            sql_code: this.sqlyuju
          }, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + this.$session.get('token')
            }
          }).then(res => {
            this.labelname2 = [],
              this.tableData3 = []
            var i;
            var lab = res.data.data[0]

            for (i in lab) {
              var tip = {
                name: lab[i],
                key: i
              }
              this.labelname2.push(tip)
            }
            var t
            for (t in res.data.data) {
              if (t > 0) {
                var result = {}
                var data = res.data.data[t]
                var ti
                for (ti in data) {
                  result[lab[ti]] = data[ti]
                }
                this.tableData3.push(result)
              }
            }

          })

        }

      },
      houyi2() {
        if (this.yeshu22 == this.yeshu12) {
          this.$message({
            message: '后面没有了，向前看看吧',
            type: 'warning'
          });
        } else {
          this.yeshu22 = this.yeshu22 + 1;
          axios.post('http://82.156.173.187:8040/page2', {
            page: this.yeshu22,
            sql_code: this.sqlyuju
          }, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + this.$session.get('token')
            }
          }).then(res => {
            this.labelname2 = [],
              this.tableData3 = []
            var i;
            var lab = res.data.data[0]

            for (i in lab) {
              var tip = {
                name: lab[i],
                key: i
              }
              this.labelname2.push(tip)
            }
            var t
            for (t in res.data.data) {
              if (t > 0) {
                var result = {}
                var data = res.data.data[t]
                var ti
                for (ti in data) {
                  result[lab[ti]] = data[ti]
                }
                this.tableData3.push(result)
              }
            }

          })

        }

      },
      tiaozhuan2() {
        if (this.yeshu32 < 1) {
          this.$message({
            message: '无法到达指定页数，请重新输入',
            type: 'warning'
          });
        } else {
          if (this.yeshu32 > this.yeshu12) {
            this.$message({
              message: '无法到达指定页数，请重新输入',
              type: 'warning'
            });
          } else {
            this.yeshu22 = Number(this.yeshu32);
            axios.post('http://82.156.173.187:8040/page2', {
              page: this.yeshu22,
              sql_code: this.sqlyuju
            }, {
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + this.$session.get('token')
              }
            }).then(res => {
              this.labelname2 = [],
                this.tableData3 = []
              var i;
              var lab = res.data.data[0]

              for (i in lab) {
                var tip = {
                  name: lab[i],
                  key: i
                }
                this.labelname2.push(tip)
              }
              var t
              for (t in res.data.data) {
                if (t > 0) {
                  var result = {}
                  var data = res.data.data[t]
                  var ti
                  for (ti in data) {
                    result[lab[ti]] = data[ti]
                  }
                  this.tableData3.push(result)
                }
              }

            })

          }
        }

      },
      qianyi() {
        if (this.yeshu2 == 1) {
          this.$message({
            message: '前面没有了，向后看看吧',
            type: 'warning'
          });
        } else {
          this.yeshu2 = this.yeshu2 - 1;
          axios.post('http://82.156.173.187:8040/page1', {
            page: this.yeshu2,
            table_name: this.value
          }, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + this.$session.get('token')
            }
          }).then(res => {
            this.labelname = [],
              this.tableData2 = []
            var i;
            var lab = res.data.data[0]

            for (i in lab) {
              var tip = {
                name: lab[i],
                key: i
              }
              this.labelname.push(tip)
            }
            var t
            for (t in res.data.data) {
              if (t > 0) {
                var result = {}
                var data = res.data.data[t]
                var ti
                for (ti in data) {
                  result[lab[ti]] = data[ti]
                }
                this.tableData2.push(result)
              }
            }

          })

        }

      },
      houyi() {
        if (this.yeshu2 == this.yeshu1) {
          this.$message({
            message: '后面没有了，向前看看吧',
            type: 'warning'
          });
        } else {
          this.yeshu2 = this.yeshu2 + 1;
          axios.post('http://82.156.173.187:8040/page1', {
            page: this.yeshu2,
            table_name: this.value
          }, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + this.$session.get('token')
            }
          }).then(res => {
            this.labelname = [],
              this.tableData2 = []
            var i;
            var lab = res.data.data[0]

            for (i in lab) {
              var tip = {
                name: lab[i],
                key: i
              }
              this.labelname.push(tip)
            }
            var t
            for (t in res.data.data) {
              if (t > 0) {
                var result = {}
                var data = res.data.data[t]
                var ti
                for (ti in data) {
                  result[lab[ti]] = data[ti]
                }
                this.tableData2.push(result)
              }
            }

          })

        }

      },
      tiaozhuan() {
        if (this.yeshu3 < 1) {
          this.$message({
            message: '无法到达指定页数，请重新输入',
            type: 'warning'
          });
        } else {
          if (this.yeshu3 > this.yeshu1) {
            this.$message({
              message: '无法到达指定页数，请重新输入',
              type: 'warning'
            });
          } else {
            this.yeshu2 = Number(this.yeshu3);
            axios.post('http://82.156.173.187:8040/page1', {
              page: this.yeshu2,
              table_name: this.value
            }, {
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + this.$session.get('token')
              }
            }).then(res => {
              this.labelname = [],
                this.tableData2 = []
              var i;
              var lab = res.data.data[0]

              for (i in lab) {
                var tip = {
                  name: lab[i],
                  key: i
                }
                this.labelname.push(tip)
              }
              var t
              for (t in res.data.data) {
                if (t > 0) {
                  var result = {}
                  var data = res.data.data[t]
                  var ti
                  for (ti in data) {
                    result[lab[ti]] = data[ti]
                  }
                  this.tableData2.push(result)
                }
              }

            })

          }
        }

      },
      tuichu() {
        this.$router.push('/login');
      },

      lianjie() {
        axios.get('http://82.156.173.187:8040/table_names', {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + this.$session.get('token')
          }
        }).then(res => {
          this.xianshibu = true;
          var i;
          for (i in res.data) {
            let num = res.data[i];
            var m;
            for (m in num) {
              var tip = {
                value: num[m],
                label: num[m]
              };
              var it;
              for (it in this.options) {
                if (this.options[it].label == String(i)) {
                  this.options[it].options.push(tip);
                }
              }
            }
          }
        })
      },
      huoqu() {
        axios.post('http://82.156.173.187:8040/get_table', {
          table_name: this.value,
        }, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + this.$session.get('token')
          }
        }).then(res => {
          console.log(res)
          this.tiaoshu1 = res.data.num
          this.yeshu1 = res.data.pages
          console.log(res)
          var i;
          var lab = res.data.data[0]

          for (i in lab) {
            var tip = {
              name: lab[i],
              key: i
            }
            this.labelname.push(tip)
          }
          var t
          for (t in res.data.data) {
            if (t > 0) {
              var result = {}
              var data = res.data.data[t]
              var ti
              for (ti in data) {
                result[lab[ti]] = data[ti]
              }
              this.tableData2.push(result)
            }
          }
        });
      },

      zeng() {
        this.jiazai2 = true
        this.xianshi2 = false
        console.log(this.textarea1)
        if (this.textarea1[0] == 's' | this.textarea1[0] == 'S') {
          this.xianshi2 = true
        }
        axios.post('http://82.156.173.187:8040/curd', {
          sql_code: this.textarea1
        }, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + this.$session.get('token')
          }
        }).then(res => {
          console.log(res)
          if (!this.xianshi2) {
            if (res.data.status == 'failure') {
              this.$message.error(res.data.reason);
              var tip2 = {
                order: this.textarea1,
                status: 'failure'
              }
              this.tableData.push(tip2)
              this.textarea1 = ''
              this.jiazai2 = false
            } else {
              this.$message({
                message: '恭喜你，操作成功',
                type: 'success'
              });
              var tip = {
                order: this.textarea1,
                status: 'success'
              }
              this.tableData.push(tip)
              this.textarea1 = ''
              this.jiazai2 = false
            }
          } else {
            if (res.data.status == 'failure') {
              this.$message.error(res.data.reason);
              var tip3 = {
                order: this.textarea1,
                status: 'failure'
              }
              this.tableData.push(tip3)
              this.xianshi2 = false
              this.textarea1 = ''
              this.jiazai2 = false
            } else {
              console.log(res)
              this.$message({
                message: '恭喜你，操作成功',
                type: 'success'
              });
              var tip4 = {
                order: this.textarea1,
                status: 'success'
              }
              this.tableData.push(tip4)
              this.yeshu12 = res.data.pages
              this.tiaoshu12 = res.data.num
              this.sqlyuju = this.textarea1
              var i;
              var lab = res.data.data[0]
              this.labelname2 = []
              this.tableData3 = []
              for (i in lab) {
                var tip5 = {
                  name: lab[i],
                  key: i
                }
                this.labelname2.push(tip5)
              }
              var t
              for (t in res.data.data) {
                if (t > 0) {
                  var result = {}
                  var data = res.data.data[t]
                  var ti
                  for (ti in data) {
                    result[lab[ti]] = data[ti]
                  }
                  this.tableData3.push(result)
                }
              }
              this.jiazai2 = false
              this.textarea1 = ''

            }
          }
        })
      },
      gain() {
        var tip = {
          'tubiao1': this.tubiaovalue1,
          'tubiao2': '1',
          'tubiao3': '1'
        }
        if (this.tubiaovalue2 != '') {
          tip = {
            'tubiao1': this.tubiaovalue1,
            'tubiao2': this.tubiaovalue2,
            'tubiao3': '1'
          }
        }
        if (this.tubiaovalue3 != '') {
          tip = {
            'tubiao1': this.tubiaovalue1,
            'tubiao2': this.tubiaovalue2,
            'tubiao3': this.tubiaovalue3
          }
        }
        axios.post('http://82.156.173.187:8040/get_cols', {
          tip: tip,
        }, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + this.$session.get('token')
          }
        }).then(res => {
          var i = 0;
          this.biaoqian1 = res.data.tubiao1
          var len1 = res.data.tubiao1.length
          this.options2[0].options = []
          this.biaoqianvalue1 = ''
          for (i = 0; i < len1; i++) {
            var tip = {
              label: res.data.tubiao1[i],
              value: i
            }
            this.options2[0].options.push(tip)
          }
          if (res.data.tubiao2 != '1') {
            this.biaoqian2 = res.data.tubiao2
            var len2 = res.data.tubiao2.length
            this.options3[0].options = []
            this.biaoqianvalue2 = ''
            for (i = 0; i < len2; i++) {
              var tip2 = {
                label: res.data.tubiao2[i],
                value: i
              }
              this.options3[0].options.push(tip2)
            }
          }

          if (res.data.tubiao3 != '1') {
            this.biaoqian3 = res.data.tubiao3
            var len3 = res.data.tubiao3.length
            this.options4[0].options = []
            this.biaoqianvalue3 = ''
            for (i = 0; i < len3; i++) {
              var tip3 = {
                label: res.data.tubiao3[i],
                value: i
              }
              this.options4[0].options.push(tip3)
            }
          }
          this.$message({
            message: '恭喜你，操作成功',
            type: 'success'
          });
        })
      },
      over() {
        this.formInline.shuliang = '';
        this.formInline.tubiao = '';
        this.formInline.tubiao2 = '';
        this.formInline.tubiao3 = '';
        this.formInline.leixing = '';
        this.formInline.leixing2 = '';
        this.formInline.leixing3 = '';
        this.formInline.duibi = '';
        this.formInline.diqu = '';
        this.formInline.shuju = '';
        this.tubiaovalue1 = '';
        this.tubiaovalue2 = '';
        this.tubiaovalue3 = '';
        this.biaoqianvalue1 = '';
        this.biaoqianvalue2 = '';
        this.biaoqianvalue3 = '';
      },
      onSubmit() {
        if (this.biaoqian1[this.biaoqianvalue1] != '') {
          var tip = {
            'tubiao1': this.tubiaovalue1,
            'biaoqian1': this.biaoqian1[this.biaoqianvalue1],
            'tubiao2': '1',
            'biaoqian2': '1',
            'tubiao3': '1',
            'biaoqian3': '1'
          }
          if (this.tubiaovalue2 != '' & this.formInline.duibi == 1) {
            tip = {
              'tubiao1': this.tubiaovalue1,
              'biaoqian1': this.biaoqian1[this.biaoqianvalue1],
              'tubiao2': this.tubiaovalue2,
              'biaoqian2': this.biaoqian2[this.biaoqianvalue2],
              'tubiao3': '1',
              'biaoqian3': '1'
            }
          }
          if (this.tubiaovalue3 != '' & this.formInline.duibi == 1) {
            tip = {
              'tubiao1': this.tubiaovalue1,
              'biaoqian1': this.biaoqian1[this.biaoqianvalue1],
              'tubiao2': this.tubiaovalue2,
              'biaoqian2': this.biaoqian2[this.biaoqianvalue2],
              'tubiao3': this.tubiaovalue3,
              'biaoqian3': this.biaoqian3[this.biaoqianvalue3]
            }
          }
          console.log(this.labelname3)
          this.labelname3 = []
          this.tableData4 = []
          if (this.tubiaovalue1 != '' & this.biaoqian1[this.biaoqianvalue1] != '') {
            var tip2 = {
              name: this.biaoqian1[this.biaoqianvalue1],
              key: 'a'
            }
            this.labelname3.push(tip2)
          }
          if (this.tubiaovalue2 != '' & this.formInline.duibi == 1) {
            var tip3 = {
              name: this.biaoqian2[this.biaoqianvalue2],
              key: 'b'
            }
            this.labelname3.push(tip3)
          }
          if (this.tubiaovalue3 != '' & this.formInline.duibi == 1) {
            var tip4 = {
              name: this.biaoqian3[this.biaoqianvalue3],
              key: 'c'
            }
            this.labelname3.push(tip4)
          }
          this.shuqian = tip
          console.log(this.labelname3)
          axios.post('http://82.156.173.187:8040/select_cols', {
            tip: tip,
          }, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + this.$session.get('token')
            }
          }).then(res => {
            var i
            console.log(res)
            this.tableData4 = []
            var tip5 = {}
            var tip6 = {}
            var tip7 = {}
            this.tubiaoleixing = ''
            this.yeshu13 = res.data.pages
            this.tiaoshu13 = res.data.num
            if (this.tubiaovalue1 != '' & this.tubiaovalue2 == '') {
              this.type1 = res.data.biaoqian1.type
              for (i = 0; i < res.data.biaoqian1.data.length; i++) {
                tip5 = {
                  'a': res.data.biaoqian1.data[i]
                }
                this.tableData4.push(tip5)
              }
            }

            if (this.tubiaovalue2 != '' & this.tubiaovalue3 == '') {
              this.type1 = res.data.biaoqian1.type
              this.type2 = res.data.biaoqian2.type
              for (i = 0; i < res.data.biaoqian2.data.length; i++) {
                tip6 = {
                  'a': res.data.biaoqian1.data[i],
                  'b': res.data.biaoqian2.data[i]
                }
                this.tableData4.push(tip6)
              }
            }




            if (this.tubiaovalue3 != '') {
              this.type3 = res.data.biaoqian3.type
              this.type1 = res.data.biaoqian1.type
              this.type2 = res.data.biaoqian2.type
              for (i = 0; i < res.data.biaoqian1.data.length; i++) {
                tip7 = {
                  'a': res.data.biaoqian1.data[i],
                  'b': res.data.biaoqian2.data[i],
                  'c': res.data.biaoqian3.data[i]
                }
                this.tableData4.push(tip7)
              }
            }

            if (this.type2 == '1') {
              this.$message({
                message: '恭喜你，操作成功',
                type: 'success'
              });
              this.chuxian = true
              if (this.type1 == 'a') {
                this.chuxian1 = true
                this.chuxian2 = false
                this.chuxian3 = false
                this.chuxian4 = false
                this.chuxian5 = false
                this.chuxian6 = false
              }
              if (this.type1 == 'b') {
                this.chuxian1 = false
                this.chuxian2 = false
                this.chuxian3 = false
                this.chuxian4 = true
                this.chuxian5 = false
                this.chuxian6 = false
              }
            } else {
              if (this.type2 == this.type1 & this.type3 == '1') {
                this.$message({
                  message: '恭喜你，操作成功',
                  type: 'success'
                });
                this.chuxian = true
                if (this.type1 == 'a') {
                  this.chuxian2 = true
                  this.chuxian1 = false

                  this.chuxian3 = false
                  this.chuxian4 = false
                  this.chuxian5 = false
                  this.chuxian6 = false
                }
                if (this.type1 == 'b') {
                  this.chuxian5 = true
                  this.chuxian1 = false
                  this.chuxian2 = false
                  this.chuxian3 = false
                  this.chuxian4 = false

                  this.chuxian6 = false
                }
              } else {
                if (this.type2 == this.type1 & this.type3 == this.type1) {
                  this.$message({
                    message: '恭喜你，操作成功',
                    type: 'success'
                  });
                  this.chuxian = true
                  if (this.type1 == 'a') {
                    this.chuxian3 = true
                    this.chuxian1 = false
                    this.chuxian2 = false

                    this.chuxian4 = false
                    this.chuxian5 = false
                    this.chuxian6 = false
                  }
                  if (this.type1 == 'b') {
                    this.chuxian6 = true
                    this.chuxian1 = false
                    this.chuxian2 = false
                    this.chuxian3 = false
                    this.chuxian4 = false
                    this.chuxian5 = false

                  }
                } else {
                  this.$message.error('您所选数据无法画图');
                  this.chuxian = false
                  this.chuxian1 = false
                  this.chuxian2 = false
                  this.chuxian3 = false
                  this.chuxian4 = false
                  this.chuxian5 = false
                  this.chuxian6 = false
                  var myChart40 = this.$echarts.init(document.getElementById("main"))
                  myChart40.clear()
                }
              }
            }
          })
        }
      },
      draw() {
        var tip = {
          'tubiao1': this.tubiaovalue1,
          'biaoqian1': this.biaoqian1[this.biaoqianvalue1],
          'type1': this.type1,
          'tubiao2': '1',
          'biaoqian2': '1',
          'type2': this.type2,
          'tubiao3': '1',
          'biaoqian3': '1',
          'type3': this.type3
        }
        if (this.tubiaovalue2 != '') {
          tip = {
            'tubiao1': this.tubiaovalue1,
            'biaoqian1': this.biaoqian1[this.biaoqianvalue1],
            'type1': this.type1,
            'tubiao2': this.tubiaovalue2,
            'biaoqian2': this.biaoqian2[this.biaoqianvalue2],
            'type2': this.type2,
            'tubiao3': '1',
            'biaoqian3': '1',
            'type3': this.type3
          }
        }
        if (this.tubiaovalue3 != '') {
          tip = {
            'tubiao1': this.tubiaovalue1,
            'biaoqian1': this.biaoqian1[this.biaoqianvalue1],
            'type1': this.type1,
            'tubiao2': this.tubiaovalue2,
            'biaoqian2': this.biaoqian2[this.biaoqianvalue2],
            'type2': this.type2,
            'tubiao3': this.tubiaovalue3,
            'biaoqian3': this.biaoqian3[this.biaoqianvalue3],
            'type3': this.type3
          }
        }
        axios.post('http://82.156.173.187:8040/count', {
          region: this.formInline.diqu,
          tip: tip,
          tubiao: this.tubiaoleixing
        }, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + this.$session.get('token')
          }
        }).then(res => {
          console.log(res)
          if (res.data.status == 'failure') {
            this.$message.error(res.data.reason);
          } else {
            this.$message({
              message: '恭喜你，操作成功',
              type: 'success'
            });
            if (this.tubiaoleixing == '1' & this.type1 == 'a') {
              var myChart1 = this.$echarts.init(document.getElementById("main"))
              myChart1.clear()
              myChart1.setOption({
                xAxis: {
                  type: 'category',
                  data: res.data.header
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
                legend: {
                  top: '5%',
                  left: 'center'
                },
                yAxis: {
                  type: 'value'
                },
                series: [{
                  data: res.data.data,
                  type: 'line'
                }]
              })
            }
            if (this.tubiaoleixing == '2' & this.type1 == 'a') {
              var myChart2 = this.$echarts.init(document.getElementById("main"))
              myChart2.clear()
              myChart2.setOption({
                xAxis: {
                  type: 'category',
                  boundaryGap: false,
                  data: res.data.header
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
                yAxis: {
                  type: 'value'
                },
                legend: {
                  top: '5%',
                  left: 'center'
                },
                series: [{
                  data: res.data.data,
                  type: 'line',
                  areaStyle: {}
                }]
              })

            }
            if (this.tubiaoleixing == '3' & this.type1 == 'a') {
              var myChart3 = this.$echarts.init(document.getElementById("main"))
              myChart3.clear()
              myChart3.setOption({
                  xAxis: {
                    type: 'category',
                    data: res.data.header
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
                  yAxis: {
                    type: 'value'
                  },
                  legend: {
                    top: '5%',
                    left: 'center'
                  },
                  series: [{
                    data: res.data.data,
                    type: 'bar',
                    barWidth: 30
                  }]
                }

              )

            }
            if (this.tubiaoleixing == '4' & this.type1 == 'a') {
              var myChart4 = this.$echarts.init(document.getElementById("main"))
              myChart4.clear()
              myChart4.setOption({
                  polar: {
                    radius: [30, '80%']
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
                  angleAxis: {
                    max: res.data.max,
                    startAngle: 75
                  },
                  legend: {
                    top: '5%',
                    left: 'center'
                  },
                  radiusAxis: {
                    type: 'category',
                    data: res.data.header
                  },
                  tooltip: {},
                  series: {
                    type: 'bar',
                    data: res.data.data,
                    coordinateSystem: 'polar',
                    label: {
                      show: true,
                      position: 'middle',
                      formatter: '{b}: {c}'
                    }
                  }
                }

              )

            }
            if (this.tubiaoleixing == '25' & this.type1 == 'a' & this.formInline.diqu == '1') {
              console.log(res)
              const pathSymbols = {
                reindeer: 'path://M-22.788,24.521c2.08-0.986,3.611-3.905,4.984-5.892 c-2.686,2.782-5.047,5.884-9.102,7.312c-0.992,0.005-0.25-2.016,0.34-2.362l1.852-0.41c0.564-0.218,0.785-0.842,0.902-1.347 c2.133-0.727,4.91-4.129,6.031-6.194c1.748-0.7,4.443-0.679,5.734-2.293c1.176-1.468,0.393-3.992,1.215-6.557 c0.24-0.754,0.574-1.581,1.008-2.293c-0.611,0.011-1.348-0.061-1.959-0.608c-1.391-1.245-0.785-2.086-1.297-3.313 c1.684,0.744,2.5,2.584,4.426,2.586C-8.46,3.012-8.255,2.901-8.04,2.824c6.031-1.952,15.182-0.165,19.498-3.937 c1.15-3.933-1.24-9.846-1.229-9.938c0.008-0.062-1.314-0.004-1.803-0.258c-1.119-0.771-6.531-3.75-0.17-3.33 c0.314-0.045,0.943,0.259,1.439,0.435c-0.289-1.694-0.92-0.144-3.311-1.946c0,0-1.1-0.855-1.764-1.98 c-0.836-1.09-2.01-2.825-2.992-4.031c-1.523-2.476,1.367,0.709,1.816,1.108c1.768,1.704,1.844,3.281,3.232,3.983 c0.195,0.203,1.453,0.164,0.926-0.468c-0.525-0.632-1.367-1.278-1.775-2.341c-0.293-0.703-1.311-2.326-1.566-2.711 c-0.256-0.384-0.959-1.718-1.67-2.351c-1.047-1.187-0.268-0.902,0.521-0.07c0.789,0.834,1.537,1.821,1.672,2.023 c0.135,0.203,1.584,2.521,1.725,2.387c0.102-0.259-0.035-0.428-0.158-0.852c-0.125-0.423-0.912-2.032-0.961-2.083 c-0.357-0.852-0.566-1.908-0.598-3.333c0.4-2.375,0.648-2.486,0.549-0.705c0.014,1.143,0.031,2.215,0.602,3.247 c0.807,1.496,1.764,4.064,1.836,4.474c0.561,3.176,2.904,1.749,2.281-0.126c-0.068-0.446-0.109-2.014-0.287-2.862 c-0.18-0.849-0.219-1.688-0.113-3.056c0.066-1.389,0.232-2.055,0.277-2.299c0.285-1.023,0.4-1.088,0.408,0.135 c-0.059,0.399-0.131,1.687-0.125,2.655c0.064,0.642-0.043,1.768,0.172,2.486c0.654,1.928-0.027,3.496,1,3.514 c1.805-0.424,2.428-1.218,2.428-2.346c-0.086-0.704-0.121-0.843-0.031-1.193c0.221-0.568,0.359-0.67,0.312-0.076 c-0.055,0.287,0.031,0.533,0.082,0.794c0.264,1.197,0.912,0.114,1.283-0.782c0.15-0.238,0.539-2.154,0.545-2.522 c-0.023-0.617,0.285-0.645,0.309,0.01c0.064,0.422-0.248,2.646-0.205,2.334c-0.338,1.24-1.105,3.402-3.379,4.712 c-0.389,0.12-1.186,1.286-3.328,2.178c0,0,1.729,0.321,3.156,0.246c1.102-0.19,3.707-0.027,4.654,0.269 c1.752,0.494,1.531-0.053,4.084,0.164c2.26-0.4,2.154,2.391-1.496,3.68c-2.549,1.405-3.107,1.475-2.293,2.984 c3.484,7.906,2.865,13.183,2.193,16.466c2.41,0.271,5.732-0.62,7.301,0.725c0.506,0.333,0.648,1.866-0.457,2.86 c-4.105,2.745-9.283,7.022-13.904,7.662c-0.977-0.194,0.156-2.025,0.803-2.247l1.898-0.03c0.596-0.101,0.936-0.669,1.152-1.139 c3.16-0.404,5.045-3.775,8.246-4.818c-4.035-0.718-9.588,3.981-12.162,1.051c-5.043,1.423-11.449,1.84-15.895,1.111 c-3.105,2.687-7.934,4.021-12.115,5.866c-3.271,3.511-5.188,8.086-9.967,10.414c-0.986,0.119-0.48-1.974,0.066-2.385l1.795-0.618 C-22.995,25.682-22.849,25.035-22.788,24.521z',
                plane: 'path://M1.112,32.559l2.998,1.205l-2.882,2.268l-2.215-0.012L1.112,32.559z M37.803,23.96 c0.158-0.838,0.5-1.509,0.961-1.904c-0.096-0.037-0.205-0.071-0.344-0.071c-0.777-0.005-2.068-0.009-3.047-0.009 c-0.633,0-1.217,0.066-1.754,0.18l2.199,1.804H37.803z M39.738,23.036c-0.111,0-0.377,0.325-0.537,0.924h1.076 C40.115,23.361,39.854,23.036,39.738,23.036z M39.934,39.867c-0.166,0-0.674,0.705-0.674,1.986s0.506,1.986,0.674,1.986 s0.672-0.705,0.672-1.986S40.102,39.867,39.934,39.867z M38.963,38.889c-0.098-0.038-0.209-0.07-0.348-0.073 c-0.082,0-0.174,0-0.268-0.001l-7.127,4.671c0.879,0.821,2.42,1.417,4.348,1.417c0.979,0,2.27-0.006,3.047-0.01 c0.139,0,0.25-0.034,0.348-0.072c-0.646-0.555-1.07-1.643-1.07-2.967C37.891,40.529,38.316,39.441,38.963,38.889z M32.713,23.96 l-12.37-10.116l-4.693-0.004c0,0,4,8.222,4.827,10.121H32.713z M59.311,32.374c-0.248,2.104-5.305,3.172-8.018,3.172H39.629 l-25.325,16.61L9.607,52.16c0,0,6.687-8.479,7.95-10.207c1.17-1.6,3.019-3.699,3.027-6.407h-2.138 c-5.839,0-13.816-3.789-18.472-5.583c-2.818-1.085-2.396-4.04-0.031-4.04h0.039l-3.299-11.371h3.617c0,0,4.352,5.696,5.846,7.5 c2,2.416,4.503,3.678,8.228,3.87h30.727c2.17,0,4.311,0.417,6.252,1.046c3.49,1.175,5.863,2.7,7.199,4.027 C59.145,31.584,59.352,32.025,59.311,32.374z M22.069,30.408c0-0.815-0.661-1.475-1.469-1.475c-0.812,0-1.471,0.66-1.471,1.475 s0.658,1.475,1.471,1.475C21.408,31.883,22.069,31.224,22.069,30.408z M27.06,30.408c0-0.815-0.656-1.478-1.466-1.478 c-0.812,0-1.471,0.662-1.471,1.478s0.658,1.477,1.471,1.477C26.404,31.885,27.06,31.224,27.06,30.408z M32.055,30.408 c0-0.815-0.66-1.475-1.469-1.475c-0.808,0-1.466,0.66-1.466,1.475s0.658,1.475,1.466,1.475 C31.398,31.883,32.055,31.224,32.055,30.408z M37.049,30.408c0-0.815-0.658-1.478-1.467-1.478c-0.812,0-1.469,0.662-1.469,1.478 s0.656,1.477,1.469,1.477C36.389,31.885,37.049,31.224,37.049,30.408z M42.039,30.408c0-0.815-0.656-1.478-1.465-1.478 c-0.811,0-1.469,0.662-1.469,1.478s0.658,1.477,1.469,1.477C41.383,31.885,42.039,31.224,42.039,30.408z M55.479,30.565 c-0.701-0.436-1.568-0.896-2.627-1.347c-0.613,0.289-1.551,0.476-2.73,0.476c-1.527,0-1.639,2.263,0.164,2.316 C52.389,32.074,54.627,31.373,55.479,30.565z',
                train: 'path://M67.335,33.596L67.335,33.596c-0.002-1.39-1.153-3.183-3.328-4.218h-9.096v-2.07h5.371 c-4.939-2.07-11.199-4.141-14.89-4.141H19.72v12.421v5.176h38.373c4.033,0,8.457-1.035,9.142-5.176h-0.027 c0.076-0.367,0.129-0.751,0.129-1.165L67.335,33.596L67.335,33.596z M27.999,30.413h-3.105v-4.141h3.105V30.413z M35.245,30.413 h-3.104v-4.141h3.104V30.413z M42.491,30.413h-3.104v-4.141h3.104V30.413z M49.736,30.413h-3.104v-4.141h3.104V30.413z  M14.544,40.764c1.143,0,2.07-0.927,2.07-2.07V35.59V25.237c0-1.145-0.928-2.07-2.07-2.07H-9.265c-1.143,0-2.068,0.926-2.068,2.07 v10.351v3.105c0,1.144,0.926,2.07,2.068,2.07H14.544L14.544,40.764z M8.333,26.272h3.105v4.141H8.333V26.272z M1.087,26.272h3.105 v4.141H1.087V26.272z M-6.159,26.272h3.105v4.141h-3.105V26.272z M-9.265,41.798h69.352v1.035H-9.265V41.798z',
                ship: 'path://M16.678,17.086h9.854l-2.703,5.912c5.596,2.428,11.155,5.575,16.711,8.607c3.387,1.847,6.967,3.75,10.541,5.375 v-6.16l-4.197-2.763v-5.318L33.064,12.197h-11.48L20.43,15.24h-4.533l-1.266,3.286l0.781,0.345L16.678,17.086z M49.6,31.84 l0.047,1.273L27.438,20.998l0.799-1.734L49.6,31.84z M33.031,15.1l12.889,8.82l0.027,0.769L32.551,16.1L33.031,15.1z M22.377,14.045 h9.846l-1.539,3.365l-2.287-1.498h1.371l0.721-1.352h-2.023l-0.553,1.037l-0.541-0.357h-0.34l0.359-0.684h-2.025l-0.361,0.684 h-3.473L22.377,14.045z M23.695,20.678l-0.004,0.004h0.004V20.678z M24.828,18.199h-2.031l-0.719,1.358h2.029L24.828,18.199z  M40.385,34.227c-12.85-7.009-25.729-14.667-38.971-12.527c1.26,8.809,9.08,16.201,8.213,24.328 c-0.553,4.062-3.111,0.828-3.303,7.137c15.799,0,32.379,0,48.166,0l0.066-4.195l1.477-7.23 C50.842,39.812,45.393,36.961,40.385,34.227z M13.99,35.954c-1.213,0-2.195-1.353-2.195-3.035c0-1.665,0.98-3.017,2.195-3.017 c1.219,0,2.195,1.352,2.195,3.017C16.186,34.604,15.213,35.954,13.99,35.954z M23.691,20.682h-2.02l-0.588,1.351h2.023 L23.691,20.682z M19.697,18.199l-0.721,1.358h2.025l0.727-1.358H19.697z',
                car: 'path://M49.592,40.883c-0.053,0.354-0.139,0.697-0.268,0.963c-0.232,0.475-0.455,0.519-1.334,0.475 c-1.135-0.053-2.764,0-4.484,0.068c0,0.476,0.018,0.697,0.018,0.697c0.111,1.299,0.697,1.342,0.931,1.342h3.7 c0.326,0,0.628,0,0.861-0.154c0.301-0.196,0.43-0.772,0.543-1.78c0.017-0.146,0.025-0.336,0.033-0.56v-0.01 c0-0.068,0.008-0.154,0.008-0.25V41.58l0,0C49.6,41.348,49.6,41.09,49.592,40.883L49.592,40.883z M6.057,40.883 c0.053,0.354,0.137,0.697,0.268,0.963c0.23,0.475,0.455,0.519,1.334,0.475c1.137-0.053,2.762,0,4.484,0.068 c0,0.476-0.018,0.697-0.018,0.697c-0.111,1.299-0.697,1.342-0.93,1.342h-3.7c-0.328,0-0.602,0-0.861-0.154 c-0.309-0.18-0.43-0.772-0.541-1.78c-0.018-0.146-0.027-0.336-0.035-0.56v-0.01c0-0.068-0.008-0.154-0.008-0.25V41.58l0,0 C6.057,41.348,6.057,41.09,6.057,40.883L6.057,40.883z M49.867,32.766c0-2.642-0.344-5.224-0.482-5.507 c-0.104-0.207-0.766-0.749-2.271-1.773c-1.522-1.042-1.487-0.887-1.766-1.566c0.25-0.078,0.492-0.224,0.639-0.241 c0.326-0.034,0.345,0.274,1.023,0.274c0.68,0,2.152-0.18,2.453-0.48c0.301-0.303,0.396-0.405,0.396-0.672 c0-0.268-0.156-0.818-0.447-1.146c-0.293-0.327-1.541-0.49-2.273-0.585c-0.729-0.095-0.834,0-1.022,0.121 c-0.304,0.189-0.32,1.919-0.32,1.919l-0.713,0.018c-0.465-1.146-1.11-3.452-2.117-5.269c-1.103-1.979-2.256-2.599-2.737-2.754 c-0.474-0.146-0.904-0.249-4.131-0.576c-3.298-0.344-5.922-0.388-8.262-0.388c-2.342,0-4.967,0.052-8.264,0.388 c-3.229,0.336-3.66,0.43-4.133,0.576s-1.633,0.775-2.736,2.754c-1.006,1.816-1.652,4.123-2.117,5.269L9.87,23.109 c0,0-0.008-1.729-0.318-1.919c-0.189-0.121-0.293-0.225-1.023-0.121c-0.732,0.104-1.98,0.258-2.273,0.585 c-0.293,0.327-0.447,0.878-0.447,1.146c0,0.267,0.094,0.379,0.396,0.672c0.301,0.301,1.773,0.48,2.453,0.48 c0.68,0,0.697-0.309,1.023-0.274c0.146,0.018,0.396,0.163,0.637,0.241c-0.283,0.68-0.24,0.524-1.764,1.566 c-1.506,1.033-2.178,1.566-2.271,1.773c-0.139,0.283-0.482,2.865-0.482,5.508s0.189,5.02,0.189,5.86c0,0.354,0,0.976,0.076,1.565 c0.053,0.354,0.129,0.697,0.268,0.966c0.232,0.473,0.447,0.516,1.334,0.473c1.137-0.051,2.779,0,4.477,0.07 c1.135,0.043,2.297,0.086,3.33,0.11c2.582,0.051,1.826-0.379,2.928-0.36c1.102,0.016,5.447,0.196,9.424,0.196 c3.976,0,8.332-0.182,9.423-0.196c1.102-0.019,0.346,0.411,2.926,0.36c1.033-0.018,2.195-0.067,3.332-0.11 c1.695-0.062,3.348-0.121,4.477-0.07c0.886,0.043,1.103,0,1.332-0.473c0.132-0.269,0.218-0.611,0.269-0.966 c0.086-0.592,0.078-1.213,0.078-1.565C49.678,37.793,49.867,35.408,49.867,32.766L49.867,32.766z M13.219,19.735 c0.412-0.964,1.652-2.9,2.256-3.244c0.145-0.087,1.426-0.491,4.637-0.706c2.953-0.198,6.217-0.276,7.73-0.276 c1.513,0,4.777,0.078,7.729,0.276c3.201,0.215,4.502,0.611,4.639,0.706c0.775,0.533,1.842,2.28,2.256,3.244 c0.412,0.965,0.965,2.858,0.861,3.116c-0.104,0.258,0.104,0.388-1.291,0.275c-1.387-0.103-10.088-0.216-14.185-0.216 c-4.088,0-12.789,0.113-14.184,0.216c-1.395,0.104-1.188-0.018-1.291-0.275C12.254,22.593,12.805,20.708,13.219,19.735 L13.219,19.735z M16.385,30.511c-0.619,0.155-0.988,0.491-1.764,0.482c-0.775,0-2.867-0.353-3.314-0.371 c-0.447-0.017-0.842,0.302-1.076,0.362c-0.23,0.06-0.688-0.104-1.377-0.318c-0.688-0.216-1.092-0.155-1.316-1.094 c-0.232-0.93,0-2.264,0-2.264c1.488-0.068,2.928,0.069,5.621,0.826c2.693,0.758,4.191,2.213,4.191,2.213 S17.004,30.357,16.385,30.511L16.385,30.511z M36.629,37.293c-1.23,0.164-6.386,0.207-8.794,0.207c-2.412,0-7.566-0.051-8.799-0.207 c-1.256-0.164-2.891-1.67-1.764-2.865c1.523-1.627,1.24-1.576,4.701-2.023C24.967,32.018,27.239,32,27.834,32 c0.584,0,2.865,0.025,5.859,0.404c3.461,0.447,3.178,0.396,4.699,2.022C39.521,35.623,37.887,37.129,36.629,37.293L36.629,37.293z  M48.129,29.582c-0.232,0.93-0.629,0.878-1.318,1.093c-0.688,0.216-1.145,0.371-1.377,0.319c-0.231-0.053-0.627-0.371-1.074-0.361 c-0.448,0.018-2.539,0.37-3.313,0.37c-0.772,0-1.146-0.328-1.764-0.481c-0.621-0.154-0.966-0.154-0.966-0.154 s1.49-1.464,4.191-2.213c2.693-0.758,4.131-0.895,5.621-0.826C48.129,27.309,48.361,28.643,48.129,29.582L48.129,29.582z'
              };
              const labelSetting = {
                show: true,
                position: 'right',
                offset: [10, 0],
                fontSize: 16
              };
              var myChart25 = this.$echarts.init(document.getElementById("main"))
              myChart25.clear()
              myChart25.setOption({
                  legend: {
                    data: ['2015', '2016']
                  },
                  tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                      type: 'shadow'
                    }
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
                  grid: {
                    containLabel: true,
                    left: 20
                  },
                  yAxis: {
                    data: res.data.header,
                    inverse: true,
                    axisLine: {
                      show: false
                    },
                    axisTick: {
                      show: false
                    },
                    axisLabel: {
                      margin: 30,
                      fontSize: 14
                    },
                    axisPointer: {
                      label: {
                        show: true,
                        margin: 30
                      }
                    }
                  },
                  xAxis: {
                    splitLine: {
                      show: false
                    },
                    axisLabel: {
                      show: false
                    },
                    axisTick: {
                      show: false
                    },
                    axisLine: {
                      show: false
                    }
                  },
                  series: [{
                    type: 'pictorialBar',
                    label: labelSetting,
                    symbolRepeat: true,
                    symbolSize: ['80%', '60%'],
                    barCategoryGap: '40%',
                    data: [{
                        value: res.data.data[0],
                        symbol: pathSymbols.plane
                      },
                      {
                        value: res.data.data[1],
                        symbol: pathSymbols.train
                      },
                      {
                        value: res.data.data[2],
                        symbol: pathSymbols.car
                      },
                      {
                        value: res.data.data[3],
                        symbol: pathSymbols.ship
                      },
                    ]
                  }, ]
                }

              )
            }


            if (this.tubiaoleixing == '25' & this.type1 == 'a' & this.formInline.diqu == '2') {
              console.log(res)
              const pathSymbols = {
                reindeer: 'path://M-22.788,24.521c2.08-0.986,3.611-3.905,4.984-5.892 c-2.686,2.782-5.047,5.884-9.102,7.312c-0.992,0.005-0.25-2.016,0.34-2.362l1.852-0.41c0.564-0.218,0.785-0.842,0.902-1.347 c2.133-0.727,4.91-4.129,6.031-6.194c1.748-0.7,4.443-0.679,5.734-2.293c1.176-1.468,0.393-3.992,1.215-6.557 c0.24-0.754,0.574-1.581,1.008-2.293c-0.611,0.011-1.348-0.061-1.959-0.608c-1.391-1.245-0.785-2.086-1.297-3.313 c1.684,0.744,2.5,2.584,4.426,2.586C-8.46,3.012-8.255,2.901-8.04,2.824c6.031-1.952,15.182-0.165,19.498-3.937 c1.15-3.933-1.24-9.846-1.229-9.938c0.008-0.062-1.314-0.004-1.803-0.258c-1.119-0.771-6.531-3.75-0.17-3.33 c0.314-0.045,0.943,0.259,1.439,0.435c-0.289-1.694-0.92-0.144-3.311-1.946c0,0-1.1-0.855-1.764-1.98 c-0.836-1.09-2.01-2.825-2.992-4.031c-1.523-2.476,1.367,0.709,1.816,1.108c1.768,1.704,1.844,3.281,3.232,3.983 c0.195,0.203,1.453,0.164,0.926-0.468c-0.525-0.632-1.367-1.278-1.775-2.341c-0.293-0.703-1.311-2.326-1.566-2.711 c-0.256-0.384-0.959-1.718-1.67-2.351c-1.047-1.187-0.268-0.902,0.521-0.07c0.789,0.834,1.537,1.821,1.672,2.023 c0.135,0.203,1.584,2.521,1.725,2.387c0.102-0.259-0.035-0.428-0.158-0.852c-0.125-0.423-0.912-2.032-0.961-2.083 c-0.357-0.852-0.566-1.908-0.598-3.333c0.4-2.375,0.648-2.486,0.549-0.705c0.014,1.143,0.031,2.215,0.602,3.247 c0.807,1.496,1.764,4.064,1.836,4.474c0.561,3.176,2.904,1.749,2.281-0.126c-0.068-0.446-0.109-2.014-0.287-2.862 c-0.18-0.849-0.219-1.688-0.113-3.056c0.066-1.389,0.232-2.055,0.277-2.299c0.285-1.023,0.4-1.088,0.408,0.135 c-0.059,0.399-0.131,1.687-0.125,2.655c0.064,0.642-0.043,1.768,0.172,2.486c0.654,1.928-0.027,3.496,1,3.514 c1.805-0.424,2.428-1.218,2.428-2.346c-0.086-0.704-0.121-0.843-0.031-1.193c0.221-0.568,0.359-0.67,0.312-0.076 c-0.055,0.287,0.031,0.533,0.082,0.794c0.264,1.197,0.912,0.114,1.283-0.782c0.15-0.238,0.539-2.154,0.545-2.522 c-0.023-0.617,0.285-0.645,0.309,0.01c0.064,0.422-0.248,2.646-0.205,2.334c-0.338,1.24-1.105,3.402-3.379,4.712 c-0.389,0.12-1.186,1.286-3.328,2.178c0,0,1.729,0.321,3.156,0.246c1.102-0.19,3.707-0.027,4.654,0.269 c1.752,0.494,1.531-0.053,4.084,0.164c2.26-0.4,2.154,2.391-1.496,3.68c-2.549,1.405-3.107,1.475-2.293,2.984 c3.484,7.906,2.865,13.183,2.193,16.466c2.41,0.271,5.732-0.62,7.301,0.725c0.506,0.333,0.648,1.866-0.457,2.86 c-4.105,2.745-9.283,7.022-13.904,7.662c-0.977-0.194,0.156-2.025,0.803-2.247l1.898-0.03c0.596-0.101,0.936-0.669,1.152-1.139 c3.16-0.404,5.045-3.775,8.246-4.818c-4.035-0.718-9.588,3.981-12.162,1.051c-5.043,1.423-11.449,1.84-15.895,1.111 c-3.105,2.687-7.934,4.021-12.115,5.866c-3.271,3.511-5.188,8.086-9.967,10.414c-0.986,0.119-0.48-1.974,0.066-2.385l1.795-0.618 C-22.995,25.682-22.849,25.035-22.788,24.521z',
                plane: 'path://M1.112,32.559l2.998,1.205l-2.882,2.268l-2.215-0.012L1.112,32.559z M37.803,23.96 c0.158-0.838,0.5-1.509,0.961-1.904c-0.096-0.037-0.205-0.071-0.344-0.071c-0.777-0.005-2.068-0.009-3.047-0.009 c-0.633,0-1.217,0.066-1.754,0.18l2.199,1.804H37.803z M39.738,23.036c-0.111,0-0.377,0.325-0.537,0.924h1.076 C40.115,23.361,39.854,23.036,39.738,23.036z M39.934,39.867c-0.166,0-0.674,0.705-0.674,1.986s0.506,1.986,0.674,1.986 s0.672-0.705,0.672-1.986S40.102,39.867,39.934,39.867z M38.963,38.889c-0.098-0.038-0.209-0.07-0.348-0.073 c-0.082,0-0.174,0-0.268-0.001l-7.127,4.671c0.879,0.821,2.42,1.417,4.348,1.417c0.979,0,2.27-0.006,3.047-0.01 c0.139,0,0.25-0.034,0.348-0.072c-0.646-0.555-1.07-1.643-1.07-2.967C37.891,40.529,38.316,39.441,38.963,38.889z M32.713,23.96 l-12.37-10.116l-4.693-0.004c0,0,4,8.222,4.827,10.121H32.713z M59.311,32.374c-0.248,2.104-5.305,3.172-8.018,3.172H39.629 l-25.325,16.61L9.607,52.16c0,0,6.687-8.479,7.95-10.207c1.17-1.6,3.019-3.699,3.027-6.407h-2.138 c-5.839,0-13.816-3.789-18.472-5.583c-2.818-1.085-2.396-4.04-0.031-4.04h0.039l-3.299-11.371h3.617c0,0,4.352,5.696,5.846,7.5 c2,2.416,4.503,3.678,8.228,3.87h30.727c2.17,0,4.311,0.417,6.252,1.046c3.49,1.175,5.863,2.7,7.199,4.027 C59.145,31.584,59.352,32.025,59.311,32.374z M22.069,30.408c0-0.815-0.661-1.475-1.469-1.475c-0.812,0-1.471,0.66-1.471,1.475 s0.658,1.475,1.471,1.475C21.408,31.883,22.069,31.224,22.069,30.408z M27.06,30.408c0-0.815-0.656-1.478-1.466-1.478 c-0.812,0-1.471,0.662-1.471,1.478s0.658,1.477,1.471,1.477C26.404,31.885,27.06,31.224,27.06,30.408z M32.055,30.408 c0-0.815-0.66-1.475-1.469-1.475c-0.808,0-1.466,0.66-1.466,1.475s0.658,1.475,1.466,1.475 C31.398,31.883,32.055,31.224,32.055,30.408z M37.049,30.408c0-0.815-0.658-1.478-1.467-1.478c-0.812,0-1.469,0.662-1.469,1.478 s0.656,1.477,1.469,1.477C36.389,31.885,37.049,31.224,37.049,30.408z M42.039,30.408c0-0.815-0.656-1.478-1.465-1.478 c-0.811,0-1.469,0.662-1.469,1.478s0.658,1.477,1.469,1.477C41.383,31.885,42.039,31.224,42.039,30.408z M55.479,30.565 c-0.701-0.436-1.568-0.896-2.627-1.347c-0.613,0.289-1.551,0.476-2.73,0.476c-1.527,0-1.639,2.263,0.164,2.316 C52.389,32.074,54.627,31.373,55.479,30.565z',
                train: 'path://M67.335,33.596L67.335,33.596c-0.002-1.39-1.153-3.183-3.328-4.218h-9.096v-2.07h5.371 c-4.939-2.07-11.199-4.141-14.89-4.141H19.72v12.421v5.176h38.373c4.033,0,8.457-1.035,9.142-5.176h-0.027 c0.076-0.367,0.129-0.751,0.129-1.165L67.335,33.596L67.335,33.596z M27.999,30.413h-3.105v-4.141h3.105V30.413z M35.245,30.413 h-3.104v-4.141h3.104V30.413z M42.491,30.413h-3.104v-4.141h3.104V30.413z M49.736,30.413h-3.104v-4.141h3.104V30.413z  M14.544,40.764c1.143,0,2.07-0.927,2.07-2.07V35.59V25.237c0-1.145-0.928-2.07-2.07-2.07H-9.265c-1.143,0-2.068,0.926-2.068,2.07 v10.351v3.105c0,1.144,0.926,2.07,2.068,2.07H14.544L14.544,40.764z M8.333,26.272h3.105v4.141H8.333V26.272z M1.087,26.272h3.105 v4.141H1.087V26.272z M-6.159,26.272h3.105v4.141h-3.105V26.272z M-9.265,41.798h69.352v1.035H-9.265V41.798z',
                ship: 'path://M16.678,17.086h9.854l-2.703,5.912c5.596,2.428,11.155,5.575,16.711,8.607c3.387,1.847,6.967,3.75,10.541,5.375 v-6.16l-4.197-2.763v-5.318L33.064,12.197h-11.48L20.43,15.24h-4.533l-1.266,3.286l0.781,0.345L16.678,17.086z M49.6,31.84 l0.047,1.273L27.438,20.998l0.799-1.734L49.6,31.84z M33.031,15.1l12.889,8.82l0.027,0.769L32.551,16.1L33.031,15.1z M22.377,14.045 h9.846l-1.539,3.365l-2.287-1.498h1.371l0.721-1.352h-2.023l-0.553,1.037l-0.541-0.357h-0.34l0.359-0.684h-2.025l-0.361,0.684 h-3.473L22.377,14.045z M23.695,20.678l-0.004,0.004h0.004V20.678z M24.828,18.199h-2.031l-0.719,1.358h2.029L24.828,18.199z  M40.385,34.227c-12.85-7.009-25.729-14.667-38.971-12.527c1.26,8.809,9.08,16.201,8.213,24.328 c-0.553,4.062-3.111,0.828-3.303,7.137c15.799,0,32.379,0,48.166,0l0.066-4.195l1.477-7.23 C50.842,39.812,45.393,36.961,40.385,34.227z M13.99,35.954c-1.213,0-2.195-1.353-2.195-3.035c0-1.665,0.98-3.017,2.195-3.017 c1.219,0,2.195,1.352,2.195,3.017C16.186,34.604,15.213,35.954,13.99,35.954z M23.691,20.682h-2.02l-0.588,1.351h2.023 L23.691,20.682z M19.697,18.199l-0.721,1.358h2.025l0.727-1.358H19.697z',
                car: 'path://M49.592,40.883c-0.053,0.354-0.139,0.697-0.268,0.963c-0.232,0.475-0.455,0.519-1.334,0.475 c-1.135-0.053-2.764,0-4.484,0.068c0,0.476,0.018,0.697,0.018,0.697c0.111,1.299,0.697,1.342,0.931,1.342h3.7 c0.326,0,0.628,0,0.861-0.154c0.301-0.196,0.43-0.772,0.543-1.78c0.017-0.146,0.025-0.336,0.033-0.56v-0.01 c0-0.068,0.008-0.154,0.008-0.25V41.58l0,0C49.6,41.348,49.6,41.09,49.592,40.883L49.592,40.883z M6.057,40.883 c0.053,0.354,0.137,0.697,0.268,0.963c0.23,0.475,0.455,0.519,1.334,0.475c1.137-0.053,2.762,0,4.484,0.068 c0,0.476-0.018,0.697-0.018,0.697c-0.111,1.299-0.697,1.342-0.93,1.342h-3.7c-0.328,0-0.602,0-0.861-0.154 c-0.309-0.18-0.43-0.772-0.541-1.78c-0.018-0.146-0.027-0.336-0.035-0.56v-0.01c0-0.068-0.008-0.154-0.008-0.25V41.58l0,0 C6.057,41.348,6.057,41.09,6.057,40.883L6.057,40.883z M49.867,32.766c0-2.642-0.344-5.224-0.482-5.507 c-0.104-0.207-0.766-0.749-2.271-1.773c-1.522-1.042-1.487-0.887-1.766-1.566c0.25-0.078,0.492-0.224,0.639-0.241 c0.326-0.034,0.345,0.274,1.023,0.274c0.68,0,2.152-0.18,2.453-0.48c0.301-0.303,0.396-0.405,0.396-0.672 c0-0.268-0.156-0.818-0.447-1.146c-0.293-0.327-1.541-0.49-2.273-0.585c-0.729-0.095-0.834,0-1.022,0.121 c-0.304,0.189-0.32,1.919-0.32,1.919l-0.713,0.018c-0.465-1.146-1.11-3.452-2.117-5.269c-1.103-1.979-2.256-2.599-2.737-2.754 c-0.474-0.146-0.904-0.249-4.131-0.576c-3.298-0.344-5.922-0.388-8.262-0.388c-2.342,0-4.967,0.052-8.264,0.388 c-3.229,0.336-3.66,0.43-4.133,0.576s-1.633,0.775-2.736,2.754c-1.006,1.816-1.652,4.123-2.117,5.269L9.87,23.109 c0,0-0.008-1.729-0.318-1.919c-0.189-0.121-0.293-0.225-1.023-0.121c-0.732,0.104-1.98,0.258-2.273,0.585 c-0.293,0.327-0.447,0.878-0.447,1.146c0,0.267,0.094,0.379,0.396,0.672c0.301,0.301,1.773,0.48,2.453,0.48 c0.68,0,0.697-0.309,1.023-0.274c0.146,0.018,0.396,0.163,0.637,0.241c-0.283,0.68-0.24,0.524-1.764,1.566 c-1.506,1.033-2.178,1.566-2.271,1.773c-0.139,0.283-0.482,2.865-0.482,5.508s0.189,5.02,0.189,5.86c0,0.354,0,0.976,0.076,1.565 c0.053,0.354,0.129,0.697,0.268,0.966c0.232,0.473,0.447,0.516,1.334,0.473c1.137-0.051,2.779,0,4.477,0.07 c1.135,0.043,2.297,0.086,3.33,0.11c2.582,0.051,1.826-0.379,2.928-0.36c1.102,0.016,5.447,0.196,9.424,0.196 c3.976,0,8.332-0.182,9.423-0.196c1.102-0.019,0.346,0.411,2.926,0.36c1.033-0.018,2.195-0.067,3.332-0.11 c1.695-0.062,3.348-0.121,4.477-0.07c0.886,0.043,1.103,0,1.332-0.473c0.132-0.269,0.218-0.611,0.269-0.966 c0.086-0.592,0.078-1.213,0.078-1.565C49.678,37.793,49.867,35.408,49.867,32.766L49.867,32.766z M13.219,19.735 c0.412-0.964,1.652-2.9,2.256-3.244c0.145-0.087,1.426-0.491,4.637-0.706c2.953-0.198,6.217-0.276,7.73-0.276 c1.513,0,4.777,0.078,7.729,0.276c3.201,0.215,4.502,0.611,4.639,0.706c0.775,0.533,1.842,2.28,2.256,3.244 c0.412,0.965,0.965,2.858,0.861,3.116c-0.104,0.258,0.104,0.388-1.291,0.275c-1.387-0.103-10.088-0.216-14.185-0.216 c-4.088,0-12.789,0.113-14.184,0.216c-1.395,0.104-1.188-0.018-1.291-0.275C12.254,22.593,12.805,20.708,13.219,19.735 L13.219,19.735z M16.385,30.511c-0.619,0.155-0.988,0.491-1.764,0.482c-0.775,0-2.867-0.353-3.314-0.371 c-0.447-0.017-0.842,0.302-1.076,0.362c-0.23,0.06-0.688-0.104-1.377-0.318c-0.688-0.216-1.092-0.155-1.316-1.094 c-0.232-0.93,0-2.264,0-2.264c1.488-0.068,2.928,0.069,5.621,0.826c2.693,0.758,4.191,2.213,4.191,2.213 S17.004,30.357,16.385,30.511L16.385,30.511z M36.629,37.293c-1.23,0.164-6.386,0.207-8.794,0.207c-2.412,0-7.566-0.051-8.799-0.207 c-1.256-0.164-2.891-1.67-1.764-2.865c1.523-1.627,1.24-1.576,4.701-2.023C24.967,32.018,27.239,32,27.834,32 c0.584,0,2.865,0.025,5.859,0.404c3.461,0.447,3.178,0.396,4.699,2.022C39.521,35.623,37.887,37.129,36.629,37.293L36.629,37.293z  M48.129,29.582c-0.232,0.93-0.629,0.878-1.318,1.093c-0.688,0.216-1.145,0.371-1.377,0.319c-0.231-0.053-0.627-0.371-1.074-0.361 c-0.448,0.018-2.539,0.37-3.313,0.37c-0.772,0-1.146-0.328-1.764-0.481c-0.621-0.154-0.966-0.154-0.966-0.154 s1.49-1.464,4.191-2.213c2.693-0.758,4.131-0.895,5.621-0.826C48.129,27.309,48.361,28.643,48.129,29.582L48.129,29.582z'
              };
              const labelSetting = {
                show: true,
                position: 'right',
                offset: [10, 0],
                fontSize: 16
              };
              var myChart25_2 = this.$echarts.init(document.getElementById("main"))
              myChart25_2.clear()
              myChart25_2.setOption({
                  legend: {
                    data: ['2015', '2016']
                  },
                  tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                      type: 'shadow'
                    }
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
                  grid: {
                    containLabel: true,
                    left: 20
                  },
                  yAxis: {
                    data: res.data.header,
                    inverse: true,
                    axisLine: {
                      show: false
                    },
                    axisTick: {
                      show: false
                    },
                    axisLabel: {
                      margin: 30,
                      fontSize: 14
                    },
                    axisPointer: {
                      label: {
                        show: true,
                        margin: 30
                      }
                    }
                  },
                  xAxis: {
                    splitLine: {
                      show: false
                    },
                    axisLabel: {
                      show: false
                    },
                    axisTick: {
                      show: false
                    },
                    axisLine: {
                      show: false
                    }
                  },
                  series: [{
                    type: 'pictorialBar',
                    label: labelSetting,
                    symbolRepeat: true,
                    symbolSize: ['80%', '60%'],
                    barCategoryGap: '40%',
                    data: [{
                        value: res.data.data[0],
                        symbol: pathSymbols.plane
                      },
                      {
                        value: res.data.data[1],
                        symbol: pathSymbols.train
                      },
                      {
                        value: res.data.data[2],
                        symbol: pathSymbols.car
                      },
                      {
                        value: res.data.data[3],
                        symbol: pathSymbols.ship
                      },
                      {
                        value: res.data.data[4],
                        symbol: pathSymbols.reindeer
                      },
                      {
                        value: res.data.data[5],
                        symbol: pathSymbols.plane
                      },
                    ]
                  }, ]
                }

              )
            }
            if (this.tubiaoleixing == '5' & this.type1 == 'a') {
              var myChart5 = this.$echarts.init(document.getElementById("main"))
              myChart5.clear()
              myChart5.setOption({
                  tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                      type: 'shadow'
                    }
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
                  legend: {
                    top: '5%',
                    left: 'center'
                  },
                  grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                  },
                  xAxis: {
                    type: 'value',
                    boundaryGap: [0, 0.01]
                  },
                  yAxis: {
                    type: 'category',
                    data: res.data.header
                  },
                  series: [{
                    type: 'bar',
                    data: res.data.data
                  }]
                }

              )

            }

            if (this.tubiaoleixing == '6' & this.tubiaovalue2 != '' & this.type1 == 'a' & this.type2 == 'a' & this
              .tubiaovalue3 == '') {
              console.log(res)
              var myChart6 = this.$echarts.init(document.getElementById("main"))
              myChart6.clear()
              myChart6.setOption({
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
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
                legend: {},
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                yAxis: {
                  type: 'value'
                },
                xAxis: {
                  type: 'category',
                  data: res.data.header
                },
                series: [{
                    name: res.data.a0.name,
                    type: 'line',
                    stack: 'Total',
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'line',
                    stack: 'Total',
                    data: res.data.a1.data
                  },
                ]
              })
            }

            if (this.tubiaoleixing == '6' & this.tubiaovalue2 != '' & this.type1 == 'a' & this.type2 == 'a' & this
              .type3 == 'a' & this.tubiaovalue3 != '') {
              console.log(res)
              var myChart6_2 = this.$echarts.init(document.getElementById("main"))
              myChart6_2.clear()
              myChart6_2.setOption({
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
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
                legend: {},
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                yAxis: {
                  type: 'value'
                },
                xAxis: {
                  type: 'category',
                  data: res.data.header
                },
                series: [{
                    name: res.data.a0.name,
                    type: 'line',
                    stack: 'Total',
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'line',
                    stack: 'Total',
                    data: res.data.a1.data
                  },
                  {
                    name: res.data.a2.name,
                    type: 'line',
                    stack: 'Total',
                    data: res.data.a2.data
                  },
                ]
              })
            }

            if (this.tubiaoleixing == '7' & this.tubiaovalue2 != '' & this.type1 == 'a' & this.type2 == 'a' & this
              .tubiaovalue3 == '') {
              console.log(res)
              var myChart7 = this.$echarts.init(document.getElementById("main"))
              myChart7.clear()
              myChart7.setOption({
                color: ['#80FFA5', '#00DDFF', '#37A2FF', '#FF0087', '#FFBF00'],
                title: {
                  text: 'Gradient Stacked Area Chart'
                },
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'cross',
                    label: {
                      backgroundColor: '#6a7985'
                    }
                  }
                },
                legend: {},
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
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                xAxis: [{
                  type: 'category',
                  boundaryGap: false,
                  data: res.data.header
                }],
                yAxis: [{
                  type: 'value'
                }],
                series: [{
                    name: res.data.a0.name,
                    type: 'line',
                    stack: 'Total',
                    smooth: true,
                    lineStyle: {
                      width: 0
                    },
                    showSymbol: false,
                    areaStyle: {
                      opacity: 0.8,
                      color: 'rgb(1, 191, 236)'
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'line',
                    stack: 'Total',
                    smooth: true,
                    lineStyle: {
                      width: 0
                    },
                    showSymbol: false,
                    areaStyle: {
                      opacity: 0.8,
                      color: 'rgb(77, 119, 255)'
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a1.data
                  },

                ]
              })
            }

            if (this.tubiaoleixing == '7' & this.tubiaovalue2 != '' & this.type1 == 'a' & this.type2 == 'a' & this
              .type3 == 'a' & this.tubiaovalue3 != '') {
              console.log(res)
              var myChart7_2 = this.$echarts.init(document.getElementById("main"))
              myChart7_2.clear()
              myChart7_2.setOption({
                color: ['#80FFA5', '#00DDFF', '#37A2FF', '#FF0087', '#FFBF00'],
                title: {
                  text: 'Gradient Stacked Area Chart'
                },
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'cross',
                    label: {
                      backgroundColor: '#6a7985'
                    }
                  }
                },
                legend: {},
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
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                xAxis: [{
                  type: 'category',
                  boundaryGap: false,
                  data: res.data.header
                }],
                yAxis: [{
                  type: 'value'
                }],
                series: [{
                    name: res.data.a0.name,
                    type: 'line',
                    stack: 'Total',
                    smooth: true,
                    lineStyle: {
                      width: 0
                    },
                    showSymbol: false,
                    areaStyle: {
                      opacity: 0.8,
                      color: 'rgb(1, 191, 236)'
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'line',
                    stack: 'Total',
                    smooth: true,
                    lineStyle: {
                      width: 0
                    },
                    showSymbol: false,
                    areaStyle: {
                      opacity: 0.8,
                      color: 'rgb(77, 119, 255)'
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a1.data
                  },
                  {
                    name: res.data.a2.name,
                    type: 'line',
                    stack: 'Total',
                    smooth: true,
                    lineStyle: {
                      width: 0
                    },
                    showSymbol: false,
                    areaStyle: {
                      opacity: 0.8,
                      color: 'rgb(116, 21, 219)'
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a2.data
                  },

                ]
              })
            }


            if (this.tubiaoleixing == '8' & this.type1 == 'b') {
              console.log(res)
              var myChart8 = this.$echarts.init(document.getElementById("main"))
              myChart8.clear()
              myChart8.setOption({
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
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
                legend: {},
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                yAxis: {
                  type: 'value'
                },
                xAxis: {
                  type: 'category',
                  data: res.data.header
                },
                series: [{
                    name: res.data.a0.name,
                    type: 'bar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'bar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a1.data
                  },
                  {
                    name: res.data.a2.name,
                    type: 'bar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a2.data
                  },
                  {
                    name: res.data.a3.name,
                    type: 'bar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a3.data
                  },
                  {
                    name: res.data.a4.name,
                    type: 'bar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a4.data
                  },
                  {
                    name: res.data.a5.name,
                    type: 'bar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a5.data
                  },
                  {
                    name: res.data.a6.name,
                    type: 'bar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a6.data
                  },
                  {
                    name: res.data.a7.name,
                    type: 'bar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a7.data
                  },
                ]
              })
            }
            if (this.tubiaoleixing == '9' & this.formInline.diqu == '1') {
              var myChart9 = this.$echarts.init(document.getElementById("main"))
              myChart9.clear()
              myChart9.setOption({
                  title: [{
                      subtext: '北方农村',
                      left: '16.67%',
                      top: '75%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '南方农村',
                      left: '50%',
                      top: '75%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '南方城镇',
                      left: '50%',
                      top: '40%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '北方城镇',
                      left: '16.67%',
                      top: '40%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '总体',
                      left: '83.33%',
                      top: '75%',
                      textAlign: 'center'
                    }
                  ],
                  legend: {
                    top: '5%',
                    left: 'center'
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
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                  },
                  series: [{
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.北方农村,
                      label: {
                        position: 'outer',
                        alignTo: 'none',
                        bleedMargin: 5
                      },
                      left: 0,
                      right: '66.6667%',
                      top: '30%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.南方农村,
                      label: {
                        position: 'outer',
                        alignTo: 'labelLine',
                        bleedMargin: 5
                      },
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '30%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.北方城镇,
                      label: {
                        position: 'outer',
                        alignTo: 'none',
                        bleedMargin: 5
                      },
                      left: 0,
                      right: '66.6667%',
                      top: '-40%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.南方城镇,
                      label: {
                        position: 'outer',
                        alignTo: 'labelLine',
                        bleedMargin: 5
                      },
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '-40%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.总体,
                      label: {
                        position: 'outer',
                        alignTo: 'edge',
                        margin: 20
                      },
                      left: '66.6667%',
                      right: 0,
                      top: '30%',
                      bottom: 0
                    }
                  ]
                }

              )

            }

            if (this.tubiaoleixing == '9' & this.formInline.diqu == '2') {
              var myChart9_2 = this.$echarts.init(document.getElementById("main"))
              myChart9_2.clear()
              myChart9_2.setOption({
                  title: [{
                      subtext: '东部农村',
                      left: '16.67%',
                      top: '65%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部农村',
                      left: '50%',
                      top: '65%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部城镇',
                      left: '50%',
                      top: '30%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '东部城镇',
                      left: '16.67%',
                      top: '30%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部城镇',
                      left: '83.33%',
                      top: '30%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部农村',
                      left: '83.33%',
                      top: '65%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '总体',
                      left: '16.67%',
                      top: '95%',
                      textAlign: 'center'
                    },
                  ],
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
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
                  legend: {
                    top: '5%',
                    left: 'center'
                  },
                  series: [{
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.东部城镇,
                      label: {
                        position: 'outer',
                        alignTo: 'none',
                        bleedMargin: 5
                      },
                      left: 0,
                      right: '66.6667%',
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.中部城镇,
                      label: {
                        position: 'outer',
                        alignTo: 'labelLine',
                        bleedMargin: 5
                      },
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.东部农村,
                      label: {
                        position: 'outer',
                        alignTo: 'none',
                        bleedMargin: 5
                      },
                      left: 0,
                      right: '66.6667%',
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.中部农村,
                      label: {
                        position: 'outer',
                        alignTo: 'labelLine',
                        bleedMargin: 5
                      },
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.西部农村,
                      label: {
                        position: 'outer',
                        alignTo: 'labelLine',
                        bleedMargin: 5
                      },
                      left: '66.6667%',
                      right: 0,
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '50%'],
                      data: res.data.西部城镇,
                      label: {
                        position: 'outer',
                        alignTo: 'edge',
                        margin: 20
                      },
                      left: '66.6667%',
                      right: 0,
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: '25%',
                      center: ['50%', '70%'],
                      data: res.data.总体,
                      label: {
                        position: 'outer',
                        alignTo: 'edge',
                        margin: 20
                      },
                      left: 0,
                      right: '66.6667%',
                      top: '50%',
                      bottom: 0
                    }
                  ]
                }

              )

            }

            if (this.tubiaoleixing == '10' & this.formInline.diqu == '1') {
              var myChart10 = this.$echarts.init(document.getElementById("main"))
              myChart10.clear()
              myChart10.setOption({
                  title: [{
                      subtext: '北方农村',
                      left: '16.67%',
                      top: '80%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '南方农村',
                      left: '50%',
                      top: '80%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '南方城镇',
                      left: '50%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '北方城镇',
                      left: '16.67%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '总体',
                      left: '83.33%',
                      top: '80%',
                      textAlign: 'center'
                    }
                  ],
                  legend: {
                    top: '5%',
                    left: 'center'
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
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                  },
                  series: [{
                      type: 'pie',
                      radius: ['40%', '70%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.北方农村,
                      left: 0,
                      right: '66.6667%',
                      top: '30%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '70%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.南方农村,
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '30%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '70%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.北方城镇,
                      left: 0,
                      right: '66.6667%',
                      top: '-40%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '70%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.南方城镇,
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '-40%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '70%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.总体,
                      left: '66.6667%',
                      right: 0,
                      top: '30%',
                      bottom: 0
                    }
                  ]
                }

              )

            }

            if (this.tubiaoleixing == '10' & this.formInline.diqu == '2') {
              var myChart10_2 = this.$echarts.init(document.getElementById("main"))
              myChart10_2.clear()
              myChart10_2.setOption({
                  title: [{
                      subtext: '东部农村',
                      left: '16.67%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部农村',
                      left: '50%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部城镇',
                      left: '50%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '东部城镇',
                      left: '16.67%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部城镇',
                      left: '83.33%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部农村',
                      left: '83.33%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '总体',
                      left: '16.67%',
                      top: '96%',
                      textAlign: 'center'
                    },
                  ],
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                  },
                  legend: {
                    top: '5%',
                    left: 'center'
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
                      type: 'pie',
                      radius: ['40%', '60%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.东部城镇,
                      left: 0,
                      right: '66.6667%',
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '60%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.中部城镇,
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '60%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.东部农村,
                      left: 0,
                      right: '66.6667%',
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '60%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.中部农村,
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '60%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.西部农村,
                      left: '66.6667%',
                      right: 0,
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '60%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '50%'],
                      data: res.data.西部城镇,
                      left: '66.6667%',
                      right: 0,
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: ['40%', '60%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: '40',
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      center: ['50%', '70%'],
                      data: res.data.总体,
                      left: 0,
                      right: '66.6667%',
                      top: '50%',
                      bottom: 0
                    }
                  ]
                }

              )

            }

            if (this.tubiaoleixing == '11' & this.formInline.diqu == '1') {
              var myChart11 = this.$echarts.init(document.getElementById("main"))
              myChart11.clear()
              myChart11.setOption({
                  title: [{
                      subtext: '北方农村',
                      left: '16.67%',
                      top: '80%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '南方农村',
                      left: '50%',
                      top: '80%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '南方城镇',
                      left: '50%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '北方城镇',
                      left: '16.67%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '总体',
                      left: '83.33%',
                      top: '80%',
                      textAlign: 'center'
                    }
                  ],
                  legend: {
                    top: '5%',
                    left: 'center'
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
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                  },
                  series: [{
                      type: 'pie',
                      radius: [20, 80],
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
                      center: ['50%', '50%'],
                      data: res.data.北方农村,
                      left: 0,
                      right: '66.6667%',
                      top: '30%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [20, 80],
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
                      center: ['50%', '50%'],
                      data: res.data.南方农村,
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '30%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [20, 80],
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
                      data: res.data.北方城镇,
                      center: ['50%', '50%'],
                      left: 0,
                      right: '66.6667%',
                      top: '-40%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [20, 80],
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
                      center: ['50%', '50%'],
                      data: res.data.南方城镇,
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '-40%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [20, 80],
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
                      center: ['50%', '50%'],
                      data: res.data.总体,
                      left: '66.6667%',
                      right: 0,
                      top: '30%',
                      bottom: 0
                    }
                  ]
                }

              )

            }

            if (this.tubiaoleixing == '11' & this.formInline.diqu == '2') {
              var myChart11_2 = this.$echarts.init(document.getElementById("main"))
              myChart11_2.clear()
              myChart11_2.setOption({
                  title: [{
                      subtext: '东部农村',
                      left: '16.67%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部农村',
                      left: '50%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部城镇',
                      left: '50%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '东部城镇',
                      left: '16.67%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部城镇',
                      left: '83.33%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部农村',
                      left: '83.33%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '总体',
                      left: '16.67%',
                      top: '90%',
                      textAlign: 'center'
                    },
                  ],
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
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
                  legend: {
                    top: '5%',
                    left: 'center'
                  },
                  series: [{
                      type: 'pie',
                      radius: [5, 40],
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
                      center: ['50%', '50%'],
                      data: res.data.东部城镇,
                      left: 0,
                      right: '66.6667%',
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [5, 40],
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
                      center: ['50%', '50%'],
                      data: res.data.中部城镇,
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [5, 40],
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
                      center: ['50%', '50%'],
                      data: res.data.东部农村,
                      left: 0,
                      right: '66.6667%',
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [5, 40],
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
                      center: ['50%', '50%'],
                      data: res.data.中部农村,
                      left: '33.3333%',
                      right: '33.3333%',
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [5, 40],
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
                      center: ['50%', '50%'],
                      data: res.data.西部农村,
                      left: '66.6667%',
                      right: 0,
                      top: '-60%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [5, 40],
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
                      center: ['50%', '50%'],
                      data: res.data.西部城镇,
                      left: '66.6667%',
                      right: 0,
                      top: '10%',
                      bottom: 0
                    },
                    {
                      type: 'pie',
                      radius: [5, 40],
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
                      center: ['50%', '70%'],
                      data: res.data.总体,
                      left: 0,
                      right: '66.6667%',
                      top: '50%',
                      bottom: 0
                    }
                  ]
                }

              )

            }

            if (this.tubiaoleixing == '12' & this.formInline.diqu == '1') {
              console.log(res)
              var myChart12 = this.$echarts.init(document.getElementById("main"))
              myChart12.clear()
              myChart12.setOption({
                title: [{
                    subtext: '总体',
                    left: '79.5%',
                    top: '38%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '南方城镇',
                    left: '48%',
                    top: '38%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '北方城镇',
                    left: '16.67%',
                    top: '38%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '南方农村',
                    left: '48%',
                    top: '75%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '北方农村',
                    left: '16.67%',
                    top: '75%',
                    textAlign: 'center'
                  },
                ],
                tooltip: {
                  trigger: 'item',
                  formatter: '{a} <br/>{b}: {c} ({d}%)'
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
                legend: {},
                series: [{
                    name: '总体',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.总体,
                    center: ['80%', '50%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '总体',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.总体,
                    center: ['80%', '50%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '北方城镇',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.北方城镇,
                    center: ['17.5%', '50%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '北方城镇',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.北方城镇,
                    center: ['17.5%', '50%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '南方城镇',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.南方城镇,
                    center: ['49%', '50%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '南方城镇',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.南方城镇,
                    center: ['49%', '50%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '南方农村',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.南方农村,
                    center: ['49%', '75%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '南方农村',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.南方农村,
                    center: ['49%', '75%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '北方农村',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.北方农村,
                    center: ['17.5%', '75%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '北方农村',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.北方农村,
                    center: ['17.5%', '75%'],
                    left: '0%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                ]
              })
            }


            if (this.tubiaoleixing == '12' & this.formInline.diqu == '2') {
              console.log(res)
              var myChart12_2 = this.$echarts.init(document.getElementById("main"))
              myChart12_2.clear()
              myChart12_2.setOption({
                title: [{
                    subtext: '总体',
                    left: '84%',
                    top: '35%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '西部城镇',
                    left: '60%',
                    top: '35%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '中部城镇',
                    left: '35%',
                    top: '35%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '东部城镇',
                    left: '12%',
                    top: '35%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '西部农村',
                    left: '60%',
                    top: '75%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '中部农村',
                    left: '35%',
                    top: '75%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '东部农村',
                    left: '12%',
                    top: '75%',
                    textAlign: 'center'
                  },
                ],
                tooltip: {
                  trigger: 'item',
                  formatter: '{a} <br/>{b}: {c} ({d}%)'
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
                legend: {},
                series: [{
                    name: '总体',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.总体,
                    center: ['80%', '50%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '总体',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.总体,
                    center: ['80%', '50%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '东部城镇',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.东部城镇,
                    center: ['-10%', '50%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '东部城镇',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.东部城镇,
                    center: ['-10%', '50%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '中部城镇',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.中部城镇,
                    center: ['20%', '50%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '中部城镇',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.中部城镇,
                    center: ['20%', '50%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '西部城镇',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.西部城镇,
                    center: ['50%', '50%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '西部城镇',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.西部城镇,
                    center: ['50%', '50%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '西部农村',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.西部农村,
                    center: ['50%', '75%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '西部农村',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.西部农村,
                    center: ['50%', '75%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '中部农村',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.中部农村,
                    center: ['20%', '75%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '中部农村',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.中部农村,
                    center: ['20%', '75%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '东部农村',
                    type: 'pie',
                    selectedMode: 'single',
                    radius: [0, '10%'],
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },
                    data: res.data.data1.东部农村,
                    center: ['-10%', '75%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                  {
                    name: '东部农村',
                    type: 'pie',
                    radius: ['15%', '20%'],
                    labelLine: {
                      length: 30
                    },
                    label: {
                      show: false
                    },
                    emphasis: {
                      label: {
                        show: true
                      }
                    },

                    data: res.data.data2.东部农村,
                    center: ['-10%', '75%'],
                    left: '20%',
                    right: 0,
                    top: '-60%',
                    bottom: 0
                  },
                ]
              })
            }


            if (this.tubiaoleixing == '13' & this.formInline.diqu == '1') {
              const markLineOpt = {
                data: [
                  [{
                      coord: [0, 3],
                      symbol: 'none'
                    },
                    {
                      coord: [20, 13],
                      symbol: 'none'
                    }
                  ]
                ]
              };

              var myChart13 = this.$echarts.init(document.getElementById("main"))
              myChart13.clear()
              myChart13.setOption({
                title: [{
                    subtext: '总体',
                    left: '82%',
                    top: '37%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '北方城镇',
                    left: '52%',
                    top: '37%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '南方城镇',
                    left: '19%',
                    top: '37%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '南方农村',
                    left: '19%',
                    top: '87%',
                    textAlign: 'center'
                  },
                  {
                    subtext: '北方农村',
                    left: '52%',
                    top: '87%',
                    textAlign: 'center'
                  },
                ],
                grid: [{
                    left: '7%',
                    top: '7%',
                    width: '25%',
                    height: '25%'
                  },
                  {
                    left: '40%',
                    top: '7%',
                    width: '25%',
                    height: '25%'
                  },
                  {
                    left: '70%',
                    top: '7%',
                    width: '25%',
                    height: '25%'
                  },
                  {
                    left: '7%',
                    bottom: '17%',
                    width: '25%',
                    height: '25%'
                  },
                  {
                    left: '40%',
                    bottom: '17%',
                    width: '25%',
                    height: '25%'
                  }
                ],
                tooltip: {
                  formatter: 'Group {a}: ({c})'
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
                xAxis: [{
                    gridIndex: 0,
                    min: res.data.南方城镇m[1],
                    max: res.data.南方城镇m[0]
                  },
                  {
                    gridIndex: 1,
                    min: res.data.北方城镇m[1],
                    max: res.data.北方城镇m[0]
                  },
                  {
                    gridIndex: 2,
                    min: res.data.总体m[1],
                    max: res.data.总体m[0]
                  },
                  {
                    gridIndex: 3,
                    min: res.data.南方农村m[1],
                    max: res.data.南方农村m[0]
                  },
                  {
                    gridIndex: 4,
                    min: res.data.北方农村m[1],
                    max: res.data.北方农村m[0]
                  }
                ],
                yAxis: [{
                    gridIndex: 0,
                    min: res.data.南方城镇m[3],
                    max: res.data.南方城镇m[2]
                  },
                  {
                    gridIndex: 1,
                    min: res.data.北方城镇m[3],
                    max: res.data.北方城镇m[2]
                  },
                  {
                    gridIndex: 2,
                    min: res.data.总体m[3],
                    max: res.data.总体m[2]
                  },
                  {
                    gridIndex: 3,
                    min: res.data.南方农村m[3],
                    max: res.data.南方农村m[2]
                  },
                  {
                    gridIndex: 4,
                    min: res.data.北方农村m[3],
                    max: res.data.北方农村m[2]
                  }
                ],
                series: [{
                    name: '南方城镇',
                    type: 'scatter',
                    xAxisIndex: 0,
                    yAxisIndex: 0,
                    data: res.data.南方城镇,
                    markLine: markLineOpt
                  },
                  {
                    name: '北方城镇',
                    type: 'scatter',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    data: res.data.北方城镇,
                    markLine: markLineOpt
                  },
                  {
                    name: '总体',
                    type: 'scatter',
                    xAxisIndex: 2,
                    yAxisIndex: 2,
                    data: res.data.总体,
                    markLine: markLineOpt
                  },
                  {
                    name: '南方农村',
                    type: 'scatter',
                    xAxisIndex: 3,
                    yAxisIndex: 3,
                    data: res.data.南方农村,
                    markLine: markLineOpt
                  },
                  {
                    name: '北方农村',
                    type: 'scatter',
                    xAxisIndex: 4,
                    yAxisIndex: 4,
                    data: res.data.北方农村,
                    markLine: markLineOpt
                  },
                ]
              })

            }



            if (this.tubiaoleixing == '13' & this.formInline.diqu == '2') {
              const markLineOpt = {
                data: [
                  [{
                      coord: [0, 3],
                      symbol: 'none'
                    },
                    {
                      coord: [20, 13],
                      symbol: 'none'
                    }
                  ]
                ]
              };

              var myChart13_2 = this.$echarts.init(document.getElementById("main"))
              myChart13_2.clear()
              myChart13_2.setOption({
                  title: [{
                      subtext: '总体',
                      left: '87%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部城镇',
                      left: '62%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部城镇',
                      left: '37%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '东部城镇',
                      left: '14%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部农村',
                      left: '62%',
                      top: '78%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部农村',
                      left: '37%',
                      top: '78%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '东部农村',
                      left: '14%',
                      top: '78%',
                      textAlign: 'center'
                    },
                  ],
                  grid: [{
                      left: '7%',
                      top: '10%',
                      width: '15%',
                      height: '15%'
                    },
                    {
                      left: '30%',
                      top: '10%',
                      width: '15%',
                      height: '15%'
                    },
                    {
                      left: '55%',
                      top: '10%',
                      width: '15%',
                      height: '15%'
                    },
                    {
                      left: '80%',
                      top: '10%',
                      width: '15%',
                      height: '15%'
                    },
                    {
                      left: '7%',
                      bottom: '30%',
                      width: '15%',
                      height: '15%'
                    },
                    {
                      left: '30%',
                      bottom: '30%',
                      width: '15%',
                      height: '15%'
                    },
                    {
                      left: '55%',
                      bottom: '30%',
                      width: '15%',
                      height: '15%'
                    },
                  ],
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
                  tooltip: {
                    formatter: 'Group {a}: ({c})'
                  },
                  xAxis: [{
                      gridIndex: 0,
                      min: res.data.东部城镇m[1],
                      max: res.data.东部城镇m[0]
                    },
                    {
                      gridIndex: 1,
                      min: res.data.中部城镇m[1],
                      max: res.data.中部城镇m[0]
                    },
                    {
                      gridIndex: 2,
                      min: res.data.西部城镇m[1],
                      max: res.data.西部城镇m[0]
                    },
                    {
                      gridIndex: 3,
                      min: res.data.总体m[1],
                      max: res.data.总体m[0]
                    },
                    {
                      gridIndex: 4,
                      min: res.data.东部农村m[1],
                      max: res.data.东部农村m[0]
                    },
                    {
                      gridIndex: 5,
                      min: res.data.中部农村m[1],
                      max: res.data.中部农村m[0]
                    },
                    {
                      gridIndex: 6,
                      min: res.data.西部农村m[1],
                      max: res.data.西部农村m[0]
                    },

                  ],
                  yAxis: [{
                      gridIndex: 0,
                      min: res.data.东部城镇m[3],
                      max: res.data.东部城镇m[2]
                    },
                    {
                      gridIndex: 1,
                      min: res.data.中部城镇m[3],
                      max: res.data.中部城镇m[2]
                    },
                    {
                      gridIndex: 2,
                      min: res.data.西部城镇m[3],
                      max: res.data.西部城镇m[2]
                    },
                    {
                      gridIndex: 3,
                      min: res.data.总体m[3],
                      max: res.data.总体m[2]
                    },
                    {
                      gridIndex: 4,
                      min: res.data.东部农村m[3],
                      max: res.data.东部农村m[2]
                    },
                    {
                      gridIndex: 5,
                      min: res.data.中部农村m[3],
                      max: res.data.中部农村m[2]
                    },
                    {
                      gridIndex: 6,
                      min: res.data.西部农村m[3],
                      max: res.data.西部农村m[2]
                    },
                  ],
                  series: [{
                      name: '东部城镇',
                      type: 'scatter',
                      xAxisIndex: 0,
                      yAxisIndex: 0,
                      data: res.data.东部城镇,
                      markLine: markLineOpt
                    },
                    {
                      name: '中部城镇',
                      type: 'scatter',
                      xAxisIndex: 1,
                      yAxisIndex: 1,
                      data: res.data.中部城镇,
                      markLine: markLineOpt
                    },
                    {
                      name: '西部城镇',
                      type: 'scatter',
                      xAxisIndex: 2,
                      yAxisIndex: 2,
                      data: res.data.西部城镇,
                      markLine: markLineOpt
                    },
                    {
                      name: '总体',
                      type: 'scatter',
                      xAxisIndex: 3,
                      yAxisIndex: 3,
                      data: res.data.总体,
                      markLine: markLineOpt
                    },
                    {
                      name: '东部农村',
                      type: 'scatter',
                      xAxisIndex: 4,
                      yAxisIndex: 4,
                      data: res.data.东部农村,
                      markLine: markLineOpt
                    },
                    {
                      name: '中部农村',
                      type: 'scatter',
                      xAxisIndex: 5,
                      yAxisIndex: 5,
                      data: res.data.中部农村,
                      markLine: markLineOpt
                    },
                    {
                      name: '西部农村',
                      type: 'scatter',
                      xAxisIndex: 6,
                      yAxisIndex: 6,
                      data: res.data.西部农村,
                      markLine: markLineOpt
                    },
                  ]
                }

              )
            }






            if (this.tubiaoleixing == '15' & this.tubiaovalue2 != '' & this.type1 == 'a' & this.type2 == 'a' & this
              .type3 == 'a' & this.tubiaovalue3 != '') {
              console.log(res.data.data)
              var myChart15 = this.$echarts.init(document.getElementById("main"))
              myChart15.clear()
              myChart15.setOption({
                backgroundColor: '#f7f8fa',
                legend: {},
                grid: {
                  left: '8%',
                  top: '10%'
                },
                xAxis: {
                  splitLine: {
                    lineStyle: {
                      type: 'dashed'
                    }
                  }
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
                yAxis: {
                  splitLine: {
                    lineStyle: {
                      type: 'dashed'
                    }
                  },
                  scale: true
                },
                series: [{
                    data: res.data.data[0],
                    type: 'scatter',
                    symbolSize: function (data) {
                      return Math.sqrt(data[2]) / 5e2;
                    },
                    emphasis: {
                      focus: 'series',
                      label: {
                        show: true,
                        formatter: function (param) {
                          return param.data[3];
                        },
                        position: 'top'
                      }
                    },
                    itemStyle: {}
                  },
                  {
                    data: res.data.data[1],
                    type: 'scatter',
                    symbolSize: function (data) {
                      return Math.sqrt(data[2]) / 5e2;
                    },
                    emphasis: {
                      focus: 'series',
                      label: {
                        show: true,
                        formatter: function (param) {
                          return param.data[3];
                        },
                        position: 'top'
                      }
                    },
                    itemStyle: {}
                  },
                  {
                    data: res.data.data[2],
                    type: 'scatter',
                    symbolSize: function (data) {
                      return Math.sqrt(data[2]) / 5e2;
                    },
                    emphasis: {
                      focus: 'series',
                      label: {
                        show: true,
                        formatter: function (param) {
                          return param.data[3];
                        },
                        position: 'top'
                      }
                    },
                    itemStyle: {}
                  },
                  {
                    data: res.data.data[3],
                    type: 'scatter',
                    symbolSize: function (data) {
                      return Math.sqrt(data[2]) / 5e2;
                    },
                    emphasis: {
                      focus: 'series',
                      label: {
                        show: true,
                        formatter: function (param) {
                          return param.data[3];
                        },
                        position: 'top'
                      }
                    },
                    itemStyle: {}
                  },

                ]
              })
            }


            if (this.tubiaoleixing == '16' & this.formInline.diqu == '1') {
              console.log(res)
              var myChart16 = this.$echarts.init(document.getElementById("main"))
              myChart16.clear()
              myChart16.setOption({
                  title: [{
                      subtext: '北方农村',
                      left: '16.67%',
                      top: '80%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '南方农村',
                      left: '50%',
                      top: '80%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '南方城镇',
                      left: '50%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '北方城镇',
                      left: '16.67%',
                      top: '45%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '总体',
                      left: '83.33%',
                      top: '80%',
                      textAlign: 'center'
                    }
                  ],
                  legend: {
                    top: '5%',
                    left: 'center'
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
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                  },
                  series: [{
                    type: 'funnel',
                    left: '7%',
                    top: 100,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.北方城镇.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.北方城镇.data
                  }, {
                    type: 'funnel',
                    left: '40%',
                    top: 100,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.南方城镇.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.南方城镇.data
                  }, {
                    type: 'funnel',
                    left: '7%',
                    top: 300,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.北方农村.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.北方农村.data
                  }, {
                    type: 'funnel',
                    left: '40%',
                    top: 300,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.南方农村.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.南方农村.data
                  }, {
                    type: 'funnel',
                    left: '74%',
                    top: 300,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.总体.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.总体.data
                  }, ]
                }


              )
            }

            if (this.tubiaoleixing == '16' & this.formInline.diqu == '2') {
              console.log(res)
              var myChart16_2 = this.$echarts.init(document.getElementById("main"))
              myChart16_2.clear()
              myChart16_2.setOption({
                  title: [
                    {
                      subtext: '东部农村',
                      left: '16.67%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部农村',
                      left: '50%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '中部城镇',
                      left: '50%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '东部城镇',
                      left: '16.67%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部城镇',
                      left: '83.33%',
                      top: '35%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '西部农村',
                      left: '83.33%',
                      top: '67%',
                      textAlign: 'center'
                    },
                    {
                      subtext: '总体',
                      left: '16.67%',
                      top: '96%',
                      textAlign: 'center'
                    },
                  ],
                  legend: {
                    top: '5%',
                    left: 'center'
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
                  tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                  },
                  series: [{
                    type: 'funnel',
                    left: '8%',
                    top: 80,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.东部城镇.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.东部城镇.data
                  }, {
                    type: 'funnel',
                    left: '41%',
                    top: 80,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.中部城镇.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.中部城镇.data
                  },{
                    type: 'funnel',
                    left: '74%',
                    top: 80,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.西部城镇.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.西部城镇.data
                  },{
                    type: 'funnel',
                    left: '8%',
                    top: 240,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.东部农村.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.东部农村.data
                  }, {
                    type: 'funnel',
                    left: '41%',
                    top: 240,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.中部农村.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.中部农村.data
                  },{
                    type: 'funnel',
                    left: '74%',
                    top: 240,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.西部农村.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.西部农村.data
                  },{
                    type: 'funnel',
                    left: '8%',
                    top: 400,
                    bottom: 60,
                    width: '20%',
                    height: '20%',
                    min: 0,
                    max: res.data.总体.max,
                    minSize: '0%',
                    maxSize: '60%',
                    sort: 'descending',
                    gap: 2,
                    label: {
                      show: true,
                      position: 'inside'
                    },
                    labelLine: {
                      length: 10,
                      lineStyle: {
                        width: 1,
                        type: 'solid'
                      }
                    },
                    itemStyle: {
                      borderColor: '#fff',
                      borderWidth: 1
                    },
                    emphasis: {
                      label: {
                        fontSize: 20
                      }
                    },
                    data: res.data.总体.data
                  }, ]
                }


              )
            }



            if (this.tubiaoleixing == '19') {
              console.log(res)
              var myChart19 = this.$echarts.init(document.getElementById("main"))
              myChart19.clear()
              myChart19.setOption({
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
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
                legend: {},
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                xAxis: {
                  type: 'value'
                },
                yAxis: {
                  type: 'category',
                  data: res.data.header
                },
                series: [{
                    name: res.data.a0.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a1.data
                  },
                  {
                    name: res.data.a2.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a2.data
                  },
                  {
                    name: res.data.a3.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a3.data
                  },
                  {
                    name: res.data.a4.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a4.data
                  },
                  {
                    name: res.data.a5.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a5.data
                  },
                  {
                    name: res.data.a6.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a6.data
                  },
                  {
                    name: res.data.a7.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a7.data
                  },
                  {
                    name: res.data.b0.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b0.data
                  },
                  {
                    name: res.data.b1.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b1.data
                  },
                  {
                    name: res.data.b2.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b2.data
                  },
                  {
                    name: res.data.b3.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b3.data
                  },
                  {
                    name: res.data.b4.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b4.data
                  },
                  {
                    name: res.data.b5.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b5.data
                  },
                  {
                    name: res.data.b6.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b6.data
                  },
                  {
                    name: res.data.b7.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b7.data
                  },
                  {
                    name: res.data.c0.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c0.data
                  },
                  {
                    name: res.data.c1.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c1.data
                  },
                  {
                    name: res.data.c2.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c2.data
                  },
                  {
                    name: res.data.c3.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c3.data
                  },
                  {
                    name: res.data.c4.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c4.data
                  },
                  {
                    name: res.data.c5.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c5.data
                  },
                  {
                    name: res.data.c6.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c6.data
                  },
                  {
                    name: res.data.c7.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c7.data
                  },
                ]
              })
            }
            if (this.tubiaoleixing == '20') {
              console.log(res)
              var myChart20 = this.$echarts.init(document.getElementById("main"))
              myChart20.clear()
              myChart20.setOption({
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
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
                legend: {},
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                yAxis: {
                  type: 'value'
                },
                xAxis: {
                  type: 'category',
                  data: res.data.header
                },
                series: [{
                    name: res.data.a0.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a1.data
                  },
                  {
                    name: res.data.a2.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a2.data
                  },
                  {
                    name: res.data.a3.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a3.data
                  },
                  {
                    name: res.data.a4.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a4.data
                  },
                  {
                    name: res.data.a5.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a5.data
                  },
                  {
                    name: res.data.a6.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a6.data
                  },
                  {
                    name: res.data.a7.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a7.data
                  },
                  {
                    name: res.data.b0.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b0.data
                  },
                  {
                    name: res.data.b1.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b1.data
                  },
                  {
                    name: res.data.b2.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b2.data
                  },
                  {
                    name: res.data.b3.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b3.data
                  },
                  {
                    name: res.data.b4.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b4.data
                  },
                  {
                    name: res.data.b5.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b5.data
                  },
                  {
                    name: res.data.b6.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b6.data
                  },
                  {
                    name: res.data.b7.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b7.data
                  },
                  {
                    name: res.data.c0.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c0.data
                  },
                  {
                    name: res.data.c1.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c1.data
                  },
                  {
                    name: res.data.c2.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c2.data
                  },
                  {
                    name: res.data.c3.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c3.data
                  },
                  {
                    name: res.data.c4.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c4.data
                  },
                  {
                    name: res.data.c5.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c5.data
                  },
                  {
                    name: res.data.c6.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c6.data
                  },
                  {
                    name: res.data.c7.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c7.data
                  },
                ]
              })
            }
            if (this.tubiaoleixing == '21') {
              console.log(res)
              var myChart21 = this.$echarts.init(document.getElementById("main"))
              myChart21.clear()
              myChart21.setOption({
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
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
                legend: {},
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                angleAxis: {},
                radiusAxis: {
                  type: 'category',
                  data: res.data.header,
                  z: 20
                },
                polar: {},

                series: [{
                    name: res.data.a0.name,
                    type: 'bar',
                    stack: 'total',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'bar',
                    stack: 'total',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a1.data
                  },
                  {
                    name: res.data.a2.name,
                    type: 'bar',
                    stack: 'total',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a2.data
                  },
                  {
                    name: res.data.a3.name,
                    type: 'bar',
                    stack: 'total',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a3.data
                  },
                  {
                    name: res.data.a4.name,
                    type: 'bar',
                    stack: 'total',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a4.data
                  },
                  {
                    name: res.data.a5.name,
                    type: 'bar',
                    stack: 'total',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a5.data
                  },
                  {
                    name: res.data.a6.name,
                    type: 'bar',
                    stack: 'total',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a6.data
                  },
                  {
                    name: res.data.a7.name,
                    type: 'bar',
                    stack: 'total',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a7.data
                  },
                  {
                    name: res.data.b0.name,
                    type: 'bar',
                    stack: 'total2',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b0.data
                  },
                  {
                    name: res.data.b1.name,
                    type: 'bar',
                    stack: 'total2',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b1.data
                  },
                  {
                    name: res.data.b2.name,
                    type: 'bar',
                    stack: 'total2',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b2.data
                  },
                  {
                    name: res.data.b3.name,
                    type: 'bar',
                    stack: 'total2',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b3.data
                  },
                  {
                    name: res.data.b4.name,
                    type: 'bar',
                    stack: 'total2',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b4.data
                  },
                  {
                    name: res.data.b5.name,
                    type: 'bar',
                    stack: 'total2',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b5.data
                  },
                  {
                    name: res.data.b6.name,
                    type: 'bar',
                    stack: 'total2',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b6.data
                  },
                  {
                    name: res.data.b7.name,
                    type: 'bar',
                    stack: 'total2',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b7.data
                  },
                  {
                    name: res.data.c0.name,
                    type: 'bar',
                    stack: 'total3',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c0.data
                  },
                  {
                    name: res.data.c1.name,
                    type: 'bar',
                    stack: 'total3',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c1.data
                  },
                  {
                    name: res.data.c2.name,
                    type: 'bar',
                    stack: 'total3',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c2.data
                  },
                  {
                    name: res.data.c3.name,
                    type: 'bar',
                    stack: 'total3',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c3.data
                  },
                  {
                    name: res.data.c4.name,
                    type: 'bar',
                    stack: 'total3',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c4.data
                  },
                  {
                    name: res.data.c5.name,
                    type: 'bar',
                    stack: 'total3',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c5.data
                  },
                  {
                    name: res.data.c6.name,
                    type: 'bar',
                    stack: 'total3',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c6.data
                  },
                  {
                    name: res.data.c7.name,
                    type: 'bar',
                    stack: 'total3',
                    coordinateSystem: 'polar',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c7.data
                  },
                ]
              })
            }
            if (this.tubiaoleixing == '22') {
              console.log(res)
              var myChart22 = this.$echarts.init(document.getElementById("main"))
              myChart22.clear()
              myChart22.setOption({
                tooltip: {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'shadow'
                  }
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
                legend: {},
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                xAxis: {
                  type: 'value'
                },
                yAxis: {
                  type: 'category',
                  data: res.data.header
                },
                series: [{
                    name: res.data.a0.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a0.data
                  },
                  {
                    name: res.data.a1.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a1.data
                  },
                  {
                    name: res.data.a2.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a2.data
                  },
                  {
                    name: res.data.a3.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a3.data
                  },
                  {
                    name: res.data.a4.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a4.data
                  },
                  {
                    name: res.data.a5.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a5.data
                  },
                  {
                    name: res.data.a6.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a6.data
                  },
                  {
                    name: res.data.a7.name,
                    type: 'bar',
                    stack: 'total',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.a7.data
                  },
                  {
                    name: res.data.b0.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b0.data
                  },
                  {
                    name: res.data.b1.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b1.data
                  },
                  {
                    name: res.data.b2.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b2.data
                  },
                  {
                    name: res.data.b3.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b3.data
                  },
                  {
                    name: res.data.b4.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b4.data
                  },
                  {
                    name: res.data.b5.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b5.data
                  },
                  {
                    name: res.data.b6.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b6.data
                  },
                  {
                    name: res.data.b7.name,
                    type: 'bar',
                    stack: 'total2',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.b7.data
                  },
                  {
                    name: res.data.c0.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c0.data
                  },
                  {
                    name: res.data.c1.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c1.data
                  },
                  {
                    name: res.data.c2.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c2.data
                  },
                  {
                    name: res.data.c3.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c3.data
                  },
                  {
                    name: res.data.c4.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c4.data
                  },
                  {
                    name: res.data.c5.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c5.data
                  },
                  {
                    name: res.data.c6.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c6.data
                  },
                  {
                    name: res.data.c7.name,
                    type: 'bar',
                    stack: 'total3',
                    label: {
                      show: true
                    },
                    emphasis: {
                      focus: 'series'
                    },
                    data: res.data.c7.data
                  },
                ]
              })
            }
            if (this.tubiaoleixing == '23') {
              console.log(res)
              var myChart23 = this.$echarts.init(document.getElementById("main"))
              myChart23.clear()
              myChart23.setOption({
                tooltip: {},
                visualMap: {
                  max: 20,
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
                  type: 'category',
                  data: res.data.yheader
                },
                yAxis3D: {
                  type: 'category',
                  data: res.data.xheader
                },
                zAxis3D: {
                  type: 'value'
                },
                grid3D: {
                  boxWidth: 200,
                  boxDepth: 80,
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
                  data: res.data.data.map(function (item) {
                    return {
                      value: [item[1], item[0], item[2]]
                    };
                  }),
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
            }
          }
        })
      }
    },
    data() {
      return {
        //echarts可视化
        tabPosition: 'left',
        jiazai: false,
        answer: '',
        formInline: {
          shuliang: '',
          tubiao: '',
          tubiao2: '',
          tubiao3: '',
          leixing: '',
          leixing2: '',
          leixing3: '',
          duibi: '',
          diqu: '',
          shuju: ''
        },
        //连接数据库
        options: [{
            label: '2010',
            options: []
          }, {
            label: '2012',
            options: []
          },
          {
            label: '2014',
            options: []
          },
          {
            label: '2016',
            options: []
          },
          {
            label: '2018',
            options: []
          }
        ],
        value: '',
        labelname: [],
        tableData2: [],
        //增删查改
        textarea1: '',
        tableData: [],
        jiazai2: false,
        //按钮显示
        xianshibu: false,
        xianshi2: false,
        labelname2: [],
        labelname3: [],
        tableData3: [],
        tableData4: [],
        tubiaovalue1: '',
        tubiaovalue2: '',
        tubiaovalue3: '',
        biaoqian1: '',
        biaoqian2: '',
        biaoqian3: '',
        biaoqianvalue1: '',
        biaoqianvalue2: '',
        biaoqianvalue3: '',
        options2: [{
          label: 'label',
          options: []
        }],
        options3: [{
          label: 'label',
          options: []
        }],
        options4: [{
          label: 'label',
          options: []
        }],
        options5: [{
            value: '1',
            label: '折线图'
          }, {
            value: '2',
            label: '面积图'
          }, {
            value: '3',
            label: '柱状图'
          }, {
            value: '4',
            label: '极坐标柱状图'
          }, {
            value: '5',
            label: '条形图'
          }, {
            value: '9',
            label: '饼图'
          }, {
            value: '10',
            label: '环形图'
          },
          {
            value: '16',
            label: '漏斗图'
          }, {
            value: '11',
            label: '玫瑰图'
          }, {
            value: '19',
            label: '堆积条形图'
          }, {
            value: '20',
            label: '堆积柱状图'
          }, {
            value: '21',
            label: '极坐标堆积柱状图'
          }, {
            value: '22',
            label: '堆积百分比柱状图'
          }, {
            value: '25',
            label: '象形柱状图'
          }
        ],
        options6: [{
          value: '6',
          label: '堆叠折线图'
        }, {
          value: '7',
          label: '堆叠面积图'
        }, {
          value: '12',
          label: '嵌套环形图'
        }, {
          value: '13',
          label: '散点图'
        }, {
          value: '19',
          label: '堆积条形图'
        }, {
          value: '20',
          label: '堆积柱状图'
        }, {
          value: '21',
          label: '极坐标堆积柱状图'
        }, {
          value: '22',
          label: '堆积百分比柱状图'
        }],
        options9: [{
          value: '12',
          label: '嵌套环形图'
        }, {
          value: '19',
          label: '堆积条形图'
        }, {
          value: '20',
          label: '堆积柱状图'
        }, {
          value: '21',
          label: '极坐标堆积柱状图'
        }, {
          value: '22',
          label: '堆积百分比柱状图'
        }],
        options7: [{
          value: '6',
          label: '堆叠折线图'
        }, {
          value: '7',
          label: '堆叠面积图'
        }, {
          value: '15',
          label: '气泡图'
        }, {
          value: '19',
          label: '堆积条形图'
        }, {
          value: '20',
          label: '堆积柱状图'
        }, {
          value: '21',
          label: '极坐标堆积柱状图'
        }, {
          value: '22',
          label: '堆积百分比柱状图'
        }],
        options8: [{
          value: '8',
          label: '堆叠柱状图'
        }, {
          value: '9',
          label: '饼图'
        }, {
          value: '10',
          label: '环形图'
        }, {
          value: '11',
          label: '玫瑰图'
        }, {
          value: '16',
          label: '漏斗图'
        }, {
          value: '19',
          label: '堆积条形图'
        }, {
          value: '20',
          label: '堆积柱状图'
        }, {
          value: '21',
          label: '极坐标堆积柱状图'
        }, {
          value: '22',
          label: '堆积百分比柱状图'
        }, {
          value: '23',
          label: '三维柱状图'
        }],
        options10: [{
          value: '19',
          label: '堆积条形图'
        }, {
          value: '20',
          label: '堆积柱状图'
        }, {
          value: '21',
          label: '极坐标堆积柱状图'
        }, {
          value: '22',
          label: '堆积百分比柱状图'
        }],
        tubiaoleixing: '',
        type1: '1',
        type2: '1',
        type3: '1',
        chuxian: false,
        chuxian1: false,
        chuxian2: false,
        chuxian3: false,
        chuxian4: false,
        chuxian5: false,
        chuxian6: false,
        yeshu1: 1,
        yeshu2: 1,
        yeshu3: 1,
        tiaoshu1: 0,
        yeshu12: 1,
        yeshu22: 1,
        yeshu32: 1,
        tiaoshu12: 0,
        sqlyuju: '',
        yeshu13: 1,
        yeshu23: 1,
        yeshu33: 1,
        tiaoshu13: 0,
        shuqian: {}

      };
    }
  }
</script>
<style scoped>
@media (min-width:320px) and (max-width:480px) {
  .s1{
    margin-top:5vh;
  }
  .s2{
    margin-top: 2vh;
    margin-bottom: 2vh;
  }
  .s3{
    margin-left:4%;width:30%;height:5vh
  }
  .s4{
    margin-left:6%;width:30%;height:5vh
  }
  .s5{
    margin-top: 2vh;
    margin-bottom: 2vh;
    margin-left:4%;width:30%;height:5vh
  }
    .s7{
    width:40%;
  }
    .s8{
    margin-top: 2vh;
    margin-left:8%;
  }

  .biaodan{
    margin-top:1vh;
    margin-right:2vh;
  }
    .tuichubu{
    margin-left: 70%;
  }
}
@media (min-width:480px) and (max-width:640px) {
    .s1{
    display: flex;
    margin-top:5vh;
  }
  .s2{
    margin-left: 5%;
    margin-bottom:4vh;
  }
    .tuichubu{
    margin-left: 65%;
  }
  .s3{
    margin-left:10%;width:30%;height:5vh
  }
  .s4{
    margin-left:10%;width:30%;height:5vh
  }
  .s5{
    margin-top: 2vh;
    margin-bottom: 2vh;
    margin-left:10%;width:30%;height:5vh
  }
    .s7{
    width:40%;
  }
  .s8{
    margin-top: 2vh;
    margin-left:6%;
    display: none;
  }
}
@media (min-width:640px) and (max-width:900px) {
    .s1{
    display: flex;
    margin-top:5vh;
  }
  .s2{
    margin-left: 5%;
    margin-bottom:4vh;
  }
  .s3{
    margin-left:14%;width:20%;height:5vh
  }
  .s4{
    margin-left:3%;width:20%;height:5vh
  }
  .s5{
    margin-left:3%;width:20%;height:5vh
  }

  .s7{
    width:20%;
  }
  .s9{
    display:flex
  }


    .tuichubu{
    margin-left: 70%;

  }
  
}
@media (min-width:900px) and (max-width:1350px) {
   .s1{
    display: flex;
    margin-top:5vh;
  }
  .s2{
    margin-left: 5%;
    margin-bottom:4vh;
  }
  .s3{
    margin-left:14%;width:20%;height:5vh
  }
  .s4{
    margin-left:3%;width:20%;height:5vh
  }
  .s5{
    margin-left:3%;width:20%;height:5vh
  }
  .s6{
    margin-left:28%
  }
  .s7{
    margin-left:2%;width:10%;
  }
  .s8{
    margin-left:2%
  }
    .s9{
    display:flex
  }

    .tuichubu{
    margin-left: 75%;

  }

}




@media (min-width:1350px) {
  .s1{
    display: flex;
    margin-top:5vh;
  }
    .s2{
    margin-left: 5%;
    margin-bottom:4vh;
  }
  .s3{
    margin-left:14%;width:20%;height:5vh
  }
  .s4{
    margin-left:3%;width:20%;height:5vh
  }
  .s5{
    margin-left:3%;width:20%;height:5vh
  }
    .s6{
    margin-left:28%
  }
    .s7{
    margin-left:2%;width:10%;
  }
    .s8{
    margin-left:2%
  }
    .s9{
    display:flex
  }

  .tuichubu{
    margin-left: 80%;

  }
  }
  .el-tabs__item {
    margin-top: 2vh !important;
    margin-left: 5% !important;
  }

  .img {
    margin-left: 5%;
    width: 50%;
    height: 40vh;
    background: url(https://s3.bmp.ovh/imgs/2022/02/cf28839f0f024aa3.jpg);
    background-size: cover;
    background-position: center center;
  }

  .wenzi3 {
    width: 40%;
    margin-left: 2%;
    margin-right: 2%;
    margin-top: 6vh;
    font-size: 20px;
  }

  .fengmian {
    margin-top: 5vh;
    margin-left: 3%;
    width: 30%;
    background: url(https://s3.bmp.ovh/imgs/2022/02/3b5af74baed09075.png);
    background-size: cover;
    background-position: center center;
    border-radius: 10%;
    box-shadow: 10px 10px 10px rgba(0, 0, 0, .5);
  }

  .fengmian2 {
    margin-top: 5vh;
    margin-left: 3%;
    width: 30%;
    background: url(https://s3.bmp.ovh/imgs/2022/02/8dcf5a315e8d5f03.png);
    background-size: cover;
    background-position: center center;
    border-radius: 10%;
    box-shadow: 10px 10px 10px rgba(0, 0, 0, .5);
  }

  .fengmian3 {
    margin-top: 5vh;
    margin-left: 3%;
    width: 30%;
    background: url(https://s3.bmp.ovh/imgs/2022/02/ca82a2f1e1f46555.png);
    background-size: cover;
    background-position: center center;
    border-radius: 10%;
    box-shadow: 10px 10px 10px rgba(0, 0, 0, .5);
  }

  .bg {
    background: url(https://s3.bmp.ovh/imgs/2022/02/7ebe894ddaa355cb.png);
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    overflow: hidden;
    overflow-y: hidden;
    overflow: hidden;
    overflow-y: hidden;
    min-height: 100vh;
  }
</style>
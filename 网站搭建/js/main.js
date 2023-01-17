window.onload=function(){
    
  var ajaxObj = new XMLHttpRequest();
  ajaxObj.open('get', 'http://121.41.179.109:8020/index');
  ajaxObj.send();
  ajaxObj.onreadystatechange = function () {
  if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
    var json=JSON.parse(ajaxObj.responseText);  
  times= document.getElementById("liulan")
  times.innerHTML=json.time;
    }
  }
}

function getTop(clsName){ 
    var obj = document.getElementsByClassName(clsName)[0];
    return obj.getBoundingClientRect().top;
}

function getDom(clsName){
    var obj=document.getElementsByClassName(clsName)[0];
    return obj;
}



window.addEventListener('scroll',function(){
    var scrollT=document.documentElement.scrollTop||document.body.scrollTop;

    /*第二页动画的触发*/
    if(getTop('title-2')<300){
        getDom('main_title-2').classList.add('xianshi');
        getDom('second_title-2').classList.add('xianshi');
    }
    if(getTop('title-3')<300){
        getDom('main_title-3').classList.add('xianshi');
        getDom('second_title-3').classList.add('xianshi');
    }
    if(getTop('title-4')<300){
        getDom('main_title-4').classList.add('xianshi');
        getDom('second_title-4').classList.add('xianshi');
    }
    if(getTop('title-5')<300){
        getDom('main_title-5').classList.add('xianshi');
        getDom('second_title-5').classList.add('xianshi');
    }
    if(getTop('title-6')<300){
        getDom('main_title-6').classList.add('xianshi');
    }
    if(getTop('title-7')<300){
        getDom('main_title-7').classList.add('xianshi');
        getDom('second_title-7').classList.add('xianshi');
    }
})

option1={
    baseOption:{
        toolbox:{
            show:true,
            feature: {
      dataZoom: {
        yAxisIndex: 'none'
      },
      dataView: { readOnly: false },
      magicType: { type: ['line', 'bar'] },
      restore: {},
      saveAsImage: {}
    }
        },
    timeline:{
        autoPlay:true,
        loop:true,
      data:['2010','2012','2014','2016','2018']
    },
    tooltip:{},
    xAxis:{type:'category',
data:['自来水','井水','江河湖水','矿泉水','窖水','其他']},
    yAxis:{type:'value',
    data:[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    max:1.0
    },
    legend: {
        type: 'scroll',
        orient: 'vertical',
        right:0,
        bottom:20,
    data: ['自来水','井水','江河湖水','矿泉水','窖水','其他']
  },
  emphasis: {
    focus: 'series'
  },
    series:[
        {
            name:'农村',
            type:'bar',
            showBackground: true,
      backgroundStyle: {
        color: 'rgba(180, 180, 180, 0.2)'
      },
    },
    {
        name:'城市',
        type:'bar',
        showBackground:true,
    },      {
        name:'农村',
            type:'pie',
            colcolorBy: 'data',
            radius:'30%',
            center: ['80%', '30%'],
    },
    {
        name:'城市',
            type:'pie',
            colcolorBy: 'data',
            radius:'30%',
            center: ['55%', '30%'],
    },
    ]},
    options:[{
        title:{text:'2010家庭饮用水来源调查'},
        series:[{data:[0.391213933,0.539251365,0.013517026, 0.002209514, 0.037821679, 0.015986483]},{data:[0.81894974,0.170068985,0.002393355, 0.006476137, 0.000563142, 0.001548641]},{data:[{name:'自来水',value:0.391213933},{name:'井水',value:0.539251365},{name:'江河湖水',value:0.013517026},{name:'矿泉水',value:0.002209514},{name:'窖水',value:0.037821679},{name:'其他',value:0.015986483}]},{data:[{name:'自来水',value:0.81894974},{name:'井水',value:0.170068985},{name:'江河湖水',value:0.002393355},{name:'矿泉水',value:0.006476137},{name:'窖水',value:0.000563142},{name:'其他',value:0.001548641}]}]
    },
    {
        title:{text:'2012家庭饮用水来源调查'},
        series:[{data:[0.47151277, 0.461268594,0.009402189, 0.002104968, 0.031995509, 0.02371597]},{data:[0.79553719,0.176198347,0.002809917, 0.012396694,0.003305785, 0.009752066]},{data:[{name:'自来水',value:0.47151277},{name:'井水',value:0.461268594},{name:'江河湖水',value:0.009402189},{name:'矿泉水',value:0.002104968},{name:'窖水',value:0.031995509},{name:'其他',value:0.02371597}]},{data:[{name:'自来水',value:0.79553719},{name:'井水',value:0.176198347},{name:'江河湖水',value:0.002809917},{name:'矿泉水',value:0.012396694},{name:'窖水',value:0.003305785},{name:'其他',value:0.009752066}]}]
    },
    {
        title:{text:'2014家庭饮用水来源调查'},
        series:[{data:[0.519312695, 0.339818233, 0.007668276, 0.004970179, 0.03166714, 0.096563476]},{data:[0.790690823,0.137722787,0.001472971, 0.011047282,0.000589188, 0.058476948]},{data:[{name:'自来水',value:0.519312695},{name:'井水',value:0.339818233},{name:'江河湖水',value:0.007668276},{name:'矿泉水',value:0.004970179},{name:'窖水',value:0.03166714},{name:'其他',value:0.096563476}]},{data:[{name:'自来水',value:0.790690823},{name:'井水',value:0.137722787},{name:'江河湖水',value:0.001472971},{name:'矿泉水',value: 0.011047282},{name:'窖水',value:0.000589188},{name:'其他',value: 0.058476948}]}]
    },
    {
        title:{text:'2016家庭饮用水来源调查'},
        series:[{data:[0.607195518, 0.30507225, 0.006045414, 0.003981127, 0.019610734, 0.058094957]},{data:[0.850224086,0.109729652,0.00216857, 0.019083418, 0.000722857, 0.018071418]},{data:[{name:'自来水',value:0.607195518},{name:'井水',value:0.30507225},{name:'江河湖水',value:0.006045414},{name:'矿泉水',value:0.003981127},{name:'窖水',value: 0.019610734},{name:'其他',value:0.058094957}]},{data:[{name:'自来水',value:0.850224086},{name:'井水',value:0.109729652},{name:'江河湖水',value:0.00216857},{name:'矿泉水',value:0.019083418},{name:'窖水',value:0.000722857},{name:'其他',value:0.018071418}]}]
    },
    {
        title:{text:'2018家庭饮用水来源调查'},
        series:[{data:[0.634330569, 0.264958531, 0.005627962, 0.01214455, 0.013329384, 0.069609005]},{data:[0.837151532,0.100055203,0.001794093, 0.040160088, 0.001242065, 0.019597019]},{data:[{name:'自来水',value:0.634330569},{name:'井水',value:0.264958531},{name:'江河湖水',value:0.005627962},{name:'矿泉水',value:0.01214455},{name:'窖水',value:0.013329384},{name:'其他',value: 0.069609005}]},{data:[{name:'自来水',value:0.837151532},{name:'井水',value:0.100055203},{name:'江河湖水',value:0.001794093},{name:'矿泉水',value:0.040160088},{name:'窖水',value:0.001242065},{name:'其他',value:0.019597019}]}]
    },
]

}

option2 = {
    baseOption: {
        toolbox: {
            show: true,
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                dataView: { readOnly: false },
                magicType: { type: ['line', 'bar'] },
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
        grid:{x2:100},
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
        series: [
            {
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
        title: { text: '2010南北家庭饮用水来源调查' },
        series: [{ data: [0.386, 
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
        title: { text: '2012南北家庭饮用水来源调查' },
        series: [{ data: [0.451,
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
        title: { text: '2014南北家庭饮用水来源调查' },
        series: [{ data: [0.497,
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
        title: { text: '2016南北家庭饮用水来源调查' },
        series: [{ data: [0.603,
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
        title: { text: '2018南北家庭饮用水来源调查' },
        series: [{ data: [0.640,
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

}

option3 = {
    baseOption: {
        toolbox: {
            show: true,
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                dataView: { readOnly: false },
                magicType: { type: ['line', 'bar'] },
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
        grid:{x2:100},
        yAxis: {
            type: 'category',
            data: ['东北部农村', '西部农村', '中部农村', '东部农村','东北部城市','西部城市','中部城市','东部城市']
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
        series: [
            {
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
        title: { text: '2010南北家庭饮用水来源调查' },
        series: [{ data: [0.340,
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
        title: { text: '2012南北家庭饮用水来源调查' },
        series: [{ data: [0.444,
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
        title: { text: '2014南北家庭饮用水来源调查' },
        series: [{ data: [0.468,
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
        title: { text: '2016南北家庭饮用水来源调查' },
        series: [{ data: [0.468,
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
        title: { text: '2018南北家庭饮用水来源调查' },
        series: [{ data: [0.431,
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

}

option4={
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
        name:'年份',
        type: 'category',
        data: ['2010','2012','2014','2016','2018']
      },
      yAxis3D: {
        name:'地域',
        type: 'category',
        data: ['城市','乡村']
      },
      zAxis3D: {
          name:'家庭收入',
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
      series: [
        {
          type: 'bar3D',
          data:[[0,0,21179.17],[0,1,36995.33],[1,0,37904.78],[1,1,56369.76],[2,0,42161.29],[2,1,69454.04],[3,0,57058.24],[3,1,94247.29],[4,0,60375.5],[4,1,117821.2]],
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
        }
      ]
}

option5={
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
        name:'年份',
        type: 'category',
        data: ['2012','2014','2016','2018']
      },
      yAxis3D: {
        name:'地域',
        type: 'category',
        data: ['城市','乡村']
      },
      zAxis3D: {
          name:'家庭人均收入',
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
      series: [
        {
          type: 'bar3D',
          data:[[0,0,9516.024],[0,1,17898.59],[1,0,11390.78],[1,1,23929.07],[2,0,15814.65],[2,1,31928.3],[3,0,17763.31],[3,1,42001.07]],
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
        }
      ]
}

var data=[{name:"南海诸岛",value:0},
{name: '北京', value: 62361},
{name: '天津', value: 39506},
{name: '上海', value: 64183},
{name: '重庆', value: 26386},
{name: '河北', value: 23446},
{name: '河南', value: 21964},
{name: '云南', value: 20084},
{name: '辽宁', value: 29701},
{name: '黑龙江', value: 22726},
{name: '湖南', value: 25241},
{name: '安徽', value: 23984},
{name: '山东', value: 29205},
{name: '新疆', value: 21500},
{name: '江苏', value: 38096},
{name: '浙江', value: 45840},
{name: '江西', value: 24080},
{name: '湖北', value: 25815},
{name: '广西', value: 21485},
{name: '甘肃', value: 17488},
{name: '山西', value: 21990},
{name: '内蒙古', value: 28376},
{name: '陕西', value: 22528},
{name: '吉林', value: 22798},
{name: '福建', value: 32644},
{name: '贵州', value: 18430},
{name: '广东', value: 35810},
{name: '青海', value: 20757},
{name: '西藏', value: 17286},
{name: '四川', value: 22461},
{name: '宁夏', value: 22400},
{name: '海南', value: 24579},
{name: '台湾', value: 0},
{name: '香港', value: 0},
{name: '澳门', value: 0}]
data.sort(function (a, b) {
  return a.value - b.value;
});
// 指定图表的配置项和数据
const mapOption = {
  visualMap: {
    left: 'right',
    min: 0,
    max: 64183,
    inRange: {
      // prettier-ignore
      color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    },
    text: ['High', 'Low'],
    calculable: true
  },
  title: {
    text: '中国地图'
},
  //提示框
tooltip: {},
  series: [
    {
      id: 'economy',
      type: 'map',
      roam: true,
      map: 'china',
      itemStyle:{
        normal:{
        areaColor:'rgb(5, 0, 27)',
        borderColor :'rgb(6, 121, 252)',
        borderWidth : 2
    },
        emphasis:{
            areaColor:'rgba(125,126,200,0.3)'
        } ,
        select:{
            areaColor:'rgba(125,126,200,0.3)'
        }           
},
  label:{
      emphasis:{
        show:true,
        formatter: '{b}',
        color:'rgb(255,255,255)',
        align:'center'
      },
      select:{
        show:true,
        formatter: '{b}',
        color:'rgb(255,255,255)',
        align:'center'
      }
  },
      animationDurationUpdate: 3000,
      universalTransition: true,
      data: data,
      roam:true,
    }
  ],
  
};

const barOption = {
  tooltip:{},
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
};

option7={
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
        name:'年份',
        type: 'category',
        data: ['2010','2012','2014','2016','2018']
      },
      yAxis3D: {
        name:'地域',
        type: 'category',
        data: ['北部乡村','南部乡村','北部城市','南部城市']
      },
      zAxis3D: {
          name:'家庭总收入',
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
      series: [
        {
          type: 'bar3D',
          data:[[0,2,28764 
          ],[0,3,44470 
          ],[0,0,17133 
          ],[0,1,26413 
          ],[1,2,47505 
          ],[1,3,65479 
          ],[1,0,36428 
          ],[1,1,40237 
          ],[2,2,51794  
          ],[2,3,87212 
          ],[2,0,38821 
          ],[2,1,45910 
          ],[3,2,76926 
          ],[3,3,110852 
          ],[3,0,44808 
          ],[3,1,77512 
          ],[4,2,91908 
          ],[4,3,142939 
          ],[4,0,53409 
          ],[4,1,70268 
          ]],
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
        }
      ]
}


option8={
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
        name:'年份',
        type: 'category',
        data: ['2010','2012','2014','2016','2018']
      },
      yAxis3D: {
        name:'地域',
        type: 'category',
        data: ['东北部农村','西部乡村','中部乡村','东部乡村','东北部城市','西部城市','中部城市','东部城市']
      },
      zAxis3D: {
          name:'家庭总收入',
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
      series: [
        {
          type: 'bar3D',
          data:[[0,0,19077 
          ],[0,1,14759 
          ],[0,2,19505 
          ],[0,3,32282 
          ],[0,4,28514 
          ],[0,5,29284 
          ],[0,6,31719 
          ],[0,7,46419 
          ],[1,0,33057 
          ],[1,1,34403 
          ],[1,2,41995 
          ],[1,3,40744 
          ],[1,4,43652 
          ],[1,5,48099 
          ],[1,6,51624 
          ],[1,7,68985 
          ],[2,0,37936 
          ],[2,1,34017 
          ],[2,2,44169 
          ],[2,3,49042 
          ],[2,4,49700 
          ],[2,5,46759 
          ],[2,6,57476 
          ],[2,7,95659 
          ],[3,0,40524 
          ],[3,1,48260 
          ],[3,2,53486 
          ],[3,3,81277 
          ],[3,4,67390 
          ],[3,5,68575 
          ],[3,6,96474 
          ],[3,7,116405 
          ],[4,0,51541 
          ],[4,1,53119 
          ],[4,2,61809 
          ],[4,3,71242 
          ],[4,4,87243 
          ],[4,5,98330 
          ],[4,6,98788 
          ],[4,7,149569 
          ]],
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
        }
      ]
}

option9 = {
    legend: {},
    tooltip: {
      trigger: 'axis',
      showContent: false
    },
    dataset: {
      source: [
        ['year','2010', '2012', '2014', '2016', '2018'],
        ['政府部门/党政机关/人民团体', 0.051115619
        , 0.029961927        , 0.045495905
        , 0.044166667
        , 0.050274941
      ],
        ['事业单位', 0.055578093
        , 0.034762457        , 0.020018198
        , 0.0125
        , 0.022780833
      ],
        ['国有企业', 0.054361055
        , 0.051481543        , 0.070973612
        , 0.049166667
        , 0.051846033
      ],
        ['私营企业/个体工商户', 0.642190669
        , 0.668266843        , 0.589626934
        , 0.605833333
        , 0.630793401
      ],
        ['外商/港澳台商企业', 0.034482759
        , 0.028803178        , 0.020928116
        , 0.031666667
        , 0.033354281
      ],
        ['个人/家庭',0.074239351
        , 0.117199139        , 0.204731574
        , 0.215
        , 0.187957581
      ],
        ['民办非企业组织/协会/行会/基金会/村居委会', 0.042190669
        , 0.033603708
        , 0.028207461
        , 0.014166667
        , 0.017282011
      ],
        ['其他', 0.045841785
        , 0.035921205
        , 0.020018198
        , 0.0275
        , 0.005710919
      ]
      ]
    },
    xAxis: { type: 'category' },
    yAxis: { gridIndex: 0 },
    grid: { top: '55%' },
    series: [
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: { focus: 'series' }
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
  };


  option10={
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
        name:'工作',
        type: 'category',
        data: ['政府部门/党政机关/人民团体','事业单位','国有企业','私营企业/个体工商户','外商/港澳台商企业','个人/家庭','其他']
      },
      yAxis3D: {
        name:'地域',
        type: 'category',
        data: ['北部乡村','南部乡村','北部城市','南部城市']
      },
      zAxis3D: {
          name:'工作差异',
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
      series: [
        {
          type: 'bar3D',
          data:[[0,0,0.050397878          ],[0,1,0.050096339
          ],[0,2,0.034653465
          ],[0,3,0.047520661
          ],[1,0,0.023872679
          ],[1,1,0.021194605
          ],[1,2,0.027227723
          ],[1,3,0.030991736
          ],[2,0,0.054376658
          ],[2,1,0.048169557
          ],[2,2,0.091584158
          ],[2,3,0.059917355
          ],[3,0,0.656498674
          ],[3,1,0.59344894
          ],[3,2,0.702970297
          ],[3,3,0.685950413
          ],[4,0,0.01193634
          ],[4,1,0.015414258
          ],[4,2,0.012376238
          ],[4,3,0.047520661
          ],[5,0,0.173740053
          ],[5,1,0.233140655
          ],[5,2,0.002475248
          ],[5,3,0.082644628
          ],[6,0,0.029177719
          ],[6,1,0.038535645
          ],[6,2,0.128712871
          ],[6,3,0.045454545
          ]],
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
        }
      ]
}



option11={
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
        name:'工作',
        type: 'category',
        data: ['政府部门/党政机关/人民团体','事业单位','国有企业','私营企业/个体工商户','外商/港澳台商企业','个人/家庭','其他']
      },
      yAxis3D: {
        name:'地域',
        type: 'category',
        data: ['东北部农村','西部农村','中部农村','东部农村','东北部城市','西部城市','中部城市','东部城市']
      },
      zAxis3D: {
          name:'工作差异',
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
      series: [
        {
          type: 'bar3D',
          data:[[0,0,0.073770492
          ],[0,1,0.068762279
          ],[0,2,0.0125
          ],[0,3,0.049689441
          ],[0,4,0.036697248
          ],[0,5,0.074257426
          ],[0,6,0.00921659
          ],[0,7,0.044444444
          ],[1,0,0.040983607
          ],[1,1,0.009823183
          ],[1,2,0.0125
          ],[1,3,0.046583851
          ],[1,4,0.018348624
          ],[1,5,0.024752475
          ],[1,6,0.013824885
          ],[1,7,0.044444444
          ],[2,0,0.049180328
          ],[2,1,0.053045187
          ],[2,2,0.053125
          ],[2,3,0.049689441
          ],[2,4,0.110091743
          ],[2,5,0.069306931
          ],[2,6,0.046082949
          ],[2,7,0.083333333
          ],[3,0,0.631147541
          ],[3,1,0.626719057
          ],[3,2,0.646875
          ],[3,3,0.621118012
          ],[3,4,0.71559633
          ],[3,5,0.707920792
          ],[3,6,0.695852535
          ],[3,7,0.677777778
          ],[4,0,0.016393443
          ],[4,1,0.009823183
          ],[4,2,0.025
          ],[4,3,0.00621118
          ],[4,4,0.009174312
          ],[4,5,0.012352
          ],[4,6,0.023041475
          ],[4,7,0.061111111
          ],[5,0,0.172131148
          ],[5,1,0.188605108
          ],[5,2,0.23125
          ],[5,3,0.189440994
          ],[5,4,0.091743119
          ],[5,5,0.099009901
          ],[5,6,0.138248848
          ],[5,7,0.058333333
          ],[6,0,0.016393443
          ],[6,1,0.043222004
          ],[6,2,0.01875
          ],[6,3,0.037267081
          ],[6,4,0.018348624
          ],[6,5,0.012400475
          ],[6,6,0.073732719
          ],[6,7,0.030555556
          ]],
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
        }
      ]
}

option12 = {
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
    toolbox:{
        show:true,
        feature: {
  dataZoom: {
    yAxisIndex: 'none'
  },
  dataView: { readOnly: false },
  restore: {},
  saveAsImage: {}
}
    },
    series: [
      {
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
        data: [
          { value: 0.037127072
            , name: '大学本科' },
            { value: 0.312375691
              , name: '初中' },
              { value: 0.261546961
                , name: '小学' },
          { value: 0.192265193
            , name: '文盲/半文盲' },
          
          
          { value: 0.134254144
            , name: '高中/中专/技校/职高' },
          { value: 0.059226519
            , name: '大专' },
          
          { value: 0.002762431
            , name: '硕士' },
          { value: 0.000331492
            , name: '博士' }
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
        data: [
          { value: 0.277210702
            , name: '初中' },
            { value: 0.194262383
              , name: '高中/中专/技校/职高' },

            { value: 0.151176534
                , name: '小学' },
           
           
            { value: 0.141936177
                , name: '大专' },
            { value: 0.136993661
                , name: '大学本科' },
                { value: 0.084130225
                  , name: '文盲/半文盲' },
            { value: 0.012571183
                , name: '硕士' },
            { value: 0.001396798
                , name: '博士' }
        ]
      }
    ]
  };

  option13 = {
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
    series: [
      {
        name: '文盲/半文盲',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.235136583,	0.162151994,	0.101666315,	0.06595092
        ]
      },
      {
        name: '小学',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.263256561,	0.260346125,	0.157983548,	0.144171779
        ]
      },
      {
        name: '初中',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.274772362,	0.338976674,	0.268719679,	0.286152498
        ]
      },
      {
        name: '高中/中专/技校/职高',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.130958757,	0.136568849,	0.190044294,	0.198729185
        ]
      },
      {
        name: '大专',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.057846813,	0.060195636,	0.137734655,	0.14636284
        ]
      },
      {
        name: '大学本科',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.03561864,	0.038186606	,0.131617802	,0.143295355
        ]
      },{
        name: '硕士',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.001310283,	0.002009782,	0.009546298,	0.013680105
        ]
      },{
        name: '博士',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0,	0.000554333,	0.001587407,	0.00105552
        ]
      },
      
    ]
  };

  option14 = {
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
      data: ['东北部农村',	'西部农村',	'中部农村'	,'东部农村'	,'东北部城市'	,'西部城市',	'中部城市'	,'东部城市'
      ]
    },
    series: [
      {
        name: '文盲/半文盲',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.135429262,	0.263064883,	0.128557875,	0.146239554,	0.063520871	,0.128078818,	0.069788384	,0.072513996

        ]
      },
      {
        name: '小学',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.252720677,	0.26937642,	0.277039848,	0.235376045,	0.137023593	,0.178683386,	0.157136425	,0.135430552

        ]
      },
      {
        name: '初中',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.400241838,	0.259530422,	0.345351044	,0.34354689,	0.289473684	,0.286162114,	0.281404773	,0.265795788

        ]
      },
      {
        name: '高中/中专/技校/职高',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.095525998,	0.125473365,	0.151328273,	0.148560817,	0.200544465,	0.170622481,	0.199459703	,0.203412423

        ]
      },
      {
        name: '大专',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.061668682	,0.0472103,	0.061195446,	0.078458682,	0.16061706,	0.111957009,	0.144529491,	0.152759264

        ]
      },
      {
        name: '大学本科',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.052204353,	0.032072456	,0.033629981,	0.039854225,	0.134208711	,0.113643977	,0.135425034,	0.150159691

        ]
      },{
        name: '硕士',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0.00120919	,0.002019692,	0.001897533	,0.005571031	,0.012704174,	0.008956561	,0.010355696	,0.015995734

        ]
      },{
        name: '博士',
        type: 'bar',
        stack: 'total',
        emphasis: {
          focus: 'series'
        },
        data: [0	,0.000252461,	0	,0.000928505,	0.000907441,	0.000895656	,0.000900495	,0.002132765

        ]
      },
      
    ]
  };

  option15={
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
      data:[{ name: '基因编辑', value: 1228 },
      { name: '婴儿', value: 981 },
      { name: '贺建奎', value: 363 }, {
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
  }
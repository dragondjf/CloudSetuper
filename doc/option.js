option = {
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['InstallerUI.exe', 'ExeSource.7z','1.png','2.png','3.png','Icon', 'package.json', 'index']
    },
    toolbox: {
        show : true,
        feature : {
            magicType : {show: true, type: ['stack']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'value'
        }
    ],
    yAxis : [
        {
            type : 'category',
            data : ['block']
        }
    ],
    series : [
        {
            name:'InstallerUI.ex',
            type:'bar',
            stack: '总量',
            itemStyle : { normal: {label : {show: true, position: 'insideLeft'}}},
            data:[400]
        },
        {
            name:'ExeSource.7z',
            type:'bar',
            stack: '总量',
            itemStyle : { normal: {label : {show: true, position: 'insideLeft'}}},
            data:[800]
        },
        {
            name:'1.png',
            type:'bar',
            stack: '总量',
            itemStyle : { normal: {label : {show: true, position: 'insideLeft'}}},
            data:[200]
        },
        {
            name:'2.png',
            type:'bar',
            stack: '总量',
            itemStyle : { normal: {label : {show: true, position: 'insideLeft'}}},
            data:[300]
        },
        {
            name:'3.png',
            type:'bar',
            stack: '总量',
            itemStyle : { normal: {label : {show: true, position: 'insideLeft'}}},
            data:[200]
        },
        {
            name:'icon',
            type:'bar',
            stack: '总量',
            itemStyle : { normal: {label : {show: true, position: 'insideLeft'}}},
            data:[100]
        },
        {
            name:'package.json',
            type:'bar',
            stack: '总量',
            itemStyle : { normal: {label : {show: true, position: 'insideLeft'}}},
            data:[492]
        },
       {
            name:'index',
            type:'bar',
            stack: '总量',
            itemStyle : { normal: {label : {show: true, position: 'insideRight'}}},
            data:[8]
        }
    ]
};

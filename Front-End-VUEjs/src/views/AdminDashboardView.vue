<template>
  <div class="mainclass">
    <admin-dashboard-base-view/><hr>
    <p style="padding: 0px 0px 0px 160px"><strong>Summary Status</strong></p>
    <admin-dashboard-card-view/><br><hr>
    <p style="padding: 0px 0px 0px 160px"><strong>Recent Activities</strong></p>
  

    <div class="container-fluied row">
      <div class="main-panel col-md-5" style="margin-left:170px;">
        <div class="panel-heading" style="text-align:center;">
          <h6 class="panel-title">Devices</h6>
        </div>

      </div>
      <div class="main-panel col-md-5" style="margin-left:2%;">
        <div class="panel-heading" style="text-align:center;">
          <h6 class="panel-title">Recent Logs</h6>
        </div>

      </div>
    </div>

    <div class="container-fluied row">
      <div class="panel panel-info col-md-5" style="margin-left:170px;">

        <table class="table table-hover" id="dev-table">
          <thead>
            <tr>
              <th>Type</th>
              <th>IP</th>
              <th>Protocol</th>
              <th>Status</th>
            </tr>
          </thead>
         <tr  class="scroll" v-for="item in deviceInfo" :key="item.DeviceId">
            <td> {{item.DeviceName}}</td>
            <td>{{item.DeviceIP}}</td>
            <td>{{item.DeviceModel}}</td>
            <span v-if="item.DeviceStatus">
              <td> <span class="label label-success">Up</span></td>
            </span>
            <span v-else-if="!item.DeviceStatus">
              <td> <span class="label label-danger">Down</span></td>
            </span>
          </tr>
        </table>
      </div>
      <div class="panel panel-info col-md-5" style="margin-left:2%;">
        <table class="table table-hover" id="dev-table">
          <thead>
            <tr>
              <th>Type</th>
              <th>IP</th>
              <th>Protocol</th>
              <th>Last Login</th>
              <th>Time Taken</th>

            </tr>
          </thead>
          <tr class="scroll" v-for="item in deviceInfo" :key="item.DeviceId">
              <td> {{item.DeviceName}}</td>
              <td>{{item.DeviceIP}}</td>
              <td>{{item.DeviceModel}}</td>
              <td>{{item.DeviceRecentLog}}</td>
              <td>{{item.DeviceLoginTimeTaken}} Milliseconds </td>
            </tr>
        </table>
      </div>
    </div>
    <br><hr><p style="padding: 0px 0px 0px 160px;"><strong> Network Metrics</strong></p>
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-6">
          <div class="container-fluid row">
            <div>
            
              <div class="col-lg-4 market-update-gd wid network-metrics" style="margin-left:125px">
                <div class="market-update-block clr-block-3">
                  <div class="col-md-8 market-update-left">
                    <h4>Accessibility 95%</h4>
                    <DoughnutChart :chartData="testData1"></DoughnutChart>
                  </div>
                  <div class="col-md-4 market-update-right">
                    <i class="fa fa-calendar"> </i>
                  </div>
                  <div class="clearfix"> </div>
                </div>
              </div>

              <div class="col-lg-4 market-update-gd wid">
                <div class="market-update-block clr-block-2">
                  <div class="col-md-8 market-update-left">
                    <h4>Retainability 85%</h4>
                    <DoughnutChart :chartData="testData2"></DoughnutChart>
                  </div>
                  <div class="col-md-4 market-update-right wid">
                    <i class="fa fa-calendar"></i>
                  </div>
                  <div class="clearfix"> </div>
                </div>
              </div>
              <div class="col-lg-4 market-update-gd wid"  style="margin-left:125px; padding-top:10px;">
                <div class="market-update-block clr-block-3">
                  <div class="col-md-8 market-update-left">
                    <h4>Mobility 60%</h4>
                    <DoughnutChart :chartData="testData3"></DoughnutChart>
                  </div>
                  <div class="col-md-4 market-update-right">
                    <i class="fa fa-calendar"> </i>
                  </div>
                  <div class="clearfix"> </div>
                </div>
              </div>
          
              <div class="col-lg-4 market-update-gd wid" style="padding-top:10px;">
                <div class="market-update-block clr-block-2">
                  <div class="col-md-8 market-update-left">
                    <h4>Availability 90%</h4>
                    <DoughnutChart :chartData="testData4"></DoughnutChart>
                  </div>
                  <div class="col-md-4 market-update-right">
                    <i class="fa fa-calendar"></i>
                  </div>
                  <div class="clearfix"> </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-5 chart1">
          <p style="padding-top:15px"><b> Network Traffic Statistics</b></p>
          <PieChart :chartData="testData"></PieChart>
        </div>
        <div class="col-lg-1" style="padding:0px;"></div>
      </div>
    </div>
    <br>
  </div>
</template>

<script>
  import AdminDashboardCardView from'../components/AdminDashboardCardsView.vue'
  import AdminDashboardBaseView from'../components/AdminDashboardBaseView.vue'
  import axios from 'axios'
  import { DoughnutChart,PieChart } from 'vue-chart-3';
  import { Chart, registerables } from "chart.js";
  Chart.register(...registerables);

  export default{
    name:'AdminDashboardView',
    components:{
      AdminDashboardCardView,
      AdminDashboardBaseView,
      DoughnutChart,
      PieChart
    },
    data:function(){
      return{
        userName:"ashraf",
        password:"pass",
        deviceInfo:[],
        deviceInfoArr:[],
        recentLogInfo:null,
        
        testData : {
          labels: ['UpLinks %', 'DownLinks %'],
          datasets: [
            {
              data: [35, 65],
              backgroundColor: ['#62C370', '#F8333C'],
            },
          ],
        },
        testData1: {
          datasets: [
            {
              data: [95, 5],
              backgroundColor: ['#018FFD', '#FF5733'],
            },
          ],
        },
        testData2 : {
          datasets: [
            {
              data: [85, 15],
              backgroundColor: ['#018FFD', '#FF5733'],
            },
          ],
        },
        testData3 : {
          datasets: [
            {
              data: [60, 40],
              backgroundColor: ['#018FFD', '#FF5733'],
            },
          ],
        },
        testData4 : {
          datasets: [
            {
              data: [90, 10],
              backgroundColor: ['#018FFD', '#FF5733'],
            },
          ],
        }
      }
    },
    methods:{
      getAdminList(){
        let today = new Date();
        let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate() + ' ' + today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        
        const deviceObj = {
          DeviceName: this.getDeviceType(),
          DeviceIP: window.location.hostname,
          DeviceModel: window.location.protocol,
          DeviceStatus: true,
          DeviceRecentLog: date
        }

        console.log("device type:" + deviceObj.DeviceName);
        console.log("protocol: "+ deviceObj.DeviceModel);
        console.log("hostname: "+ deviceObj.DeviceIP);
        console.log("date: "+ deviceObj.DeviceRecentLog);

        // add device info
        axios.post('/devicelist',deviceObj).then(response =>{
          console.log(response.data);
        })
        .catch(error =>{
          console.log(error)
        })

        // get device list
        axios.get('/devicelist').then(response =>{
          this.deviceInfo = response.data
          
          for (let index = 0; index < this.deviceInfo.length; index++) { // add one more dunamic column the deviesl list array in order to display
            const deviceObj = {
              DeviceName: this.deviceInfo[index].DeviceName,
              DeviceIP: this.deviceInfo[index].DeviceIP,
              DeviceModel: this.deviceInfo[index].DeviceModel,
              DeviceStatus: this.deviceInfo[index].DeviceStatus,
              DeviceRecentLog: this.deviceInfo[index].DeviceRecentLog,
              DeviceLoginTimeTaken: this.randInt(0,1000),
            }
            this.deviceInfo[index] = deviceObj;
          }
        })
        .catch(error =>{
          console.log(error)
        })

        // get device statistics
        axios.get('/devicestatistics').then(response =>{
          this.recentLogInfo = response.data
        })
        .catch(error =>{
          console.log(error)
        })

      },
      getDeviceType(){
        const ua = navigator.userAgent;
        if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {
          return "Tablet";
        }
        if (/Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(ua)) {
          return "Mobile";
        }
          return "Desktop";
      },
      randInt(low , max){
        return Math.floor(Math.random() * 100) % (max ?? low) + (max ? low : 10);
      }
    },

    created: function(){
      this.getAdminList()
    }
  }

</script>

<style scoped>
  button{
    width: 100%;
    height: 35px;
  }
  .chart1{
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius:10px;
  }
  .panel{
    overflow-y: scroll;
    height: 500px;
  }
  .main-panel{
    background-color: #c0dbd5;
    border-radius: 5px;

  }
  .mainclass{
    overflow-x: hidden;
  }

  /* width */
  ::-webkit-scrollbar {
    width: 5px;
  }

/* Track */
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 5px grey; 
    border-radius: 10px;
  }
 
/* Handle */
  ::-webkit-scrollbar-thumb {
    background: rgb(139, 135, 135); 
    border-radius: 10px;
  }

/* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: rgb(129, 125, 125); 
  }

  .market-update-block {
    padding: 2em 2em;
    background: #999;
  }

  .market-update-block h3 {
    color: #fff;
    font-size: 2.5em;
    font-family: 'Carrois Gothic', sans-serif;
  }

  .market-update-block h4 {
    font-size: 1.2em;
    color: #fff;
    margin: 0.3em 0em;
    font-family: 'Carrois Gothic', sans-serif;
  }

  .market-update-block {
    padding: .5em;
    background: rgb(8, 8, 8);
    border-radius:10px;

  }

  .market-update-block p {
    color: rgb(248, 248, 248);
    font-size: 0.8em;
    line-height: 1.8em;
  }

  .market-update-right i.fa.fa-user-o {
    font-size: 3em;
  }

  .market-update-right i.fa.fa-calendar {
    font-size: 3em;
  }
  .market-update-left {
    padding: 0px;
  }
</style>
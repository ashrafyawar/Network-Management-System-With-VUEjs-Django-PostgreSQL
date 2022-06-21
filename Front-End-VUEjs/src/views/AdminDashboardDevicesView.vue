<template>
  <div class="mainclass">    
    <admin-dashboard-base-view/><hr>
    <p style="padding: 0px 0px 0px 160px"><strong>Summary Status</strong></p>
    <admin-dashboard-card-view/><br><hr>
    <p style="padding: 0px 0px 0px 160px"><strong>Real-Time Network Statistics</strong></p>
  
    <div class="container-fluied row">
      <div class="col-md-5 chart1" style="margin-left:170px;">
          <p style="padding-top:15px"><b>Connected Devices Per Each Month</b></p>
          <LineChart :chartData="logsPerMonthsData"></LineChart>
      </div>
      <div class="col-md-5 chart1" style="margin-left:2%;">
          <p style="padding-top:15px"><b>Network Activity Statistics</b></p>
          <BarChart :chartData="networkPingedCounterPerMonthData"></BarChart>
      </div>
    </div>
    <br><hr>
    <p style="padding: 0px 0px 0px 160px"><strong>Real-Time Devices Informations</strong></p>

    <div class="container-fluied row">
      <div class="col-md-1"></div>
      <div class="main-panel col-md-8" style="margin-left:170px;">
        <div class="panel-heading" style="text-align:center;">
          <h4 class="panel-danger"><strong>Currently UP And RUNNING Devices On This Network</strong> </h4>
        </div>
      </div>
    </div>

    <div class="container-fluied row">
      <div class="col-md-1"></div>
      <div class="panel panel-info col-md-8" style="margin-left:170px;">
        <table class="table table-hover" id="dev-table">
          <thead>
            <tr>
              <th>Type</th>
              <th>IP</th>
              <th>Protocol</th>
              <th>Last Login Time</th>
              <th>Time Taken</th>
              <th>Status</th>
            </tr>
          </thead>
         <tr  class="scroll" v-for="item in deviceInfo" :key="item.DeviceId">
            <td> {{item.DeviceName}}</td>
            <td>{{item.DeviceIP}}</td>
            <td>{{item.DeviceModel}}</td>
            <td>{{item.DeviceRecentLog}}</td>
            <td>{{item.DeviceLoginTimeTaken}} Milliseconds</td>
            <span v-if="item.DeviceStatus">
              <td> <span class="label label-success">Up</span></td>
            </span>
            <span v-else-if="!item.DeviceStatus">
              <td> <span class="label label-danger">Down</span></td>
            </span>
          </tr>
        </table>
        
      </div>
      <br><br><br><br> <div class="col-md-2"></div>
    </div>

    <div class="container-fluied row">
      <div class="col-md-1"></div>
      <div class="col-md-8" style="margin-left:170px;">
      </div>
      <br><br><br><br> <div class="col-md-2"></div>


      <div class="content">
        <form class="container" id="myFrom">
          <label>Device Type</label>
          <input 
            type="text" 
            v-model="deviceType"
            name="name"
            placeholder="Enter Device Type Here"
          >
          <label>Ip Address</label>
          <input 
            type="text" 
            v-model="deviceIP"
            name="text"
            placeholder="Enter Device IP Address Here"
            >
          <label>Protocol Type</label>
          <input 
            type="text" 
            v-model="deviceProtocolType"
            name="text"
            placeholder="Enter Device IP Address Here"
            >
          <button type="button" class="btn btn-secondary btn-lg btn-block" @click="addDeviceButton($event)"> <strong style="color:white"> Add Device To The Network </strong></button>
        </form>
      </div>
    </div>
    <br><hr>
  </div>
</template>

<script>
  import AdminDashboardCardView from'../components/AdminDashboardCardsView.vue'
  import AdminDashboardBaseView from'../components/AdminDashboardBaseView.vue'
  import axios from 'axios'
  import { LineChart,BarChart } from 'vue-chart-3';
  import { Chart, registerables } from "chart.js";
  Chart.register(...registerables);

 export default{
    name:'AdminDashboardDevicesView',
    components:{
      AdminDashboardCardView,
      AdminDashboardBaseView,
      LineChart,
      BarChart,
    },
    data:function(){
        return{
          deviceType:"",
          deviceIP:"",
          deviceProtocolType:"",
          
          deviceInfo:[],
          riskyIpList:[],
          logsPerMonthsData : {
          labels: ['January', 'Febriuary','March','April','May','June','July','August','September','October','November','December'],
          datasets: [{	
            label: "DEVICES vs MONTHS",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [35, 65,98,25,11,150,101,115,77,84,10,22],
            }],
        },
        networkPingedCounterPerMonthData : {
          labels: ['January', 'Febriuary','March','April','May','June','July','August','September','October','November','December'],
          datasets: [{	
            label: "PING-TESTS vs MONTHS",
            backgroundColor: 'rgb(13, 206, 100)',
            borderColor: 'rgb(13, 206, 100)',
            data: [150, 65,98,111,11,451,101,115,784,84,10,22],
            }],
        },
        }
    },
    methods:{
      
      getBlcokedIPList(){
          // get the risky ip list
          axios.get('/blockedip').then(response =>{
            this.riskyIpList = response.data;
          })
          .catch(error =>{
            console.log(error)
          })
      }
      ,
      getDeviceList(){
        axios.get('/devicelist').then(response =>{
          this.deviceInfo = response.data
          for (let index = 0; index < this.deviceInfo.length; index++) { // add one more dunamic column the deviesl list array in order to display
            const deviceObj = {
              DeviceName: this.deviceInfo[index].DeviceName,
              DeviceIP: this.deviceInfo[index].DeviceIP,
              DeviceModel: this.deviceInfo[index].DeviceModel,
              DeviceStatus: true,
              DeviceRecentLog: this.deviceInfo[index].DeviceRecentLog,
              DeviceLoginTimeTaken: this.randInt(0,1000),
            }
            this.deviceInfo[index] = deviceObj;
          }
        })
        .catch(error =>{
          console.log(error)
        })
      },
     
     randInt(low , max){
        return Math.floor(Math.random() * 100) % (max ?? low) + (max ? low : 10);
      },

      addDeviceButton(e) {
        if (this.deviceType != "" && this.deviceIP != "" && this.deviceProtocolType !="") { // save device into the system
          let isExist = false;
          for (let index = 0; index < this.riskyIpList.length; index++) {
            if (this.riskyIpList[index].IP == this.deviceIP) {
              isExist = true;
              break;
            }
          }

          if (isExist === true) {
            alert("IP Of " + this.deviceIP + " Is Blcoked By The System !!!")
          }else{
            let today = new Date();
            let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate() + ' ' + today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

            const deviceInfo = {
              DeviceName:this.deviceType,
              DeviceIP:this.deviceIP,
              DeviceModel:this.deviceProtocolType,
              DeviceStatus: false,
              DeviceRecentLog:date,
            }
            axios.post('/postdevice',deviceInfo).then(response =>{
              console.log(response);
            })
            .catch(error =>{
              console.log(error)
            })
            alert("Device Is Added Successfully Into The System :)")
            this.getDeviceList()
            this.getBlcokedIPList()
            window.location.reload();
          }
        }
        else {
          alert("Fill In The DeviceType,DeviceIP And Device Protocol Fields !!!")
        }
      },
    },
    created: function(){
      this.getDeviceList()
      this.getBlcokedIPList()
    }
  }

</script>

<style scoped>

  * {box-sizing: border-box;}
  .submit-button{
    width: 25%;
  }
  .container {
    overflow: hidden;
    display: block;
    margin:auto;
    text-align: center;
    border-radius: 5px;
    background-color: #caa8a8;
    padding: 20px;
    /* width: 50%; */
  }

  label {
    float: left;
  }

  input[type=text], [type=email], textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid rgb(48, 43, 43);
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
    resize: vertical;
  }

  input[type=submit] {
    background-color: #4CAF50;
    color: rgb(39, 31, 31);
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
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
    background: rgb(187, 152, 152); 
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
    background: rgb(218, 162, 162);
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
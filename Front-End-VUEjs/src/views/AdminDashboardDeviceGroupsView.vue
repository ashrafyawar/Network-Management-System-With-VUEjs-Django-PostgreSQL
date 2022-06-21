<template>
  <div class="mainclass">    
    <admin-dashboard-base-view/>
    <p style="padding: 0px 0px 0px 160px"><strong>Summary Status</strong></p>
    <admin-dashboard-card-view/><br><hr>   
    <p style="padding: 0px 0px 0px 160px"><strong>Security Actions</strong></p>
  
    <div class="container-fluied row">
      <div class="col-md-1"></div>
      <div class="main-panel col-md-8" style="margin-left:170px;">
        <div class="panel-heading" style="text-align:center;">
          <h4 class="panel-danger"><strong>POTENTIAL RISKY DEVICES ON THIS NETWORK</strong> </h4>
        </div>
      </div>
    </div>

    <div class="container-fluied row">
      <div class="col-md-1"></div>
      <div class="panel panel-info col-md-8" style="margin-left:170px;">
        <table class="table table-hover">
          <thead>
            <tr >
              <th> Device IP</th>
              <th>Device Type</th>
              <th>Suspicious Activity Description</th>
              <th>Risk Priority</th>
              <th>Take Action</th>
            </tr>
          </thead>
         <tr  class="scroll" v-for="item in riskyDeviceList" :key="item.DeviceId">
            <td> {{item.DeviceIP}}</td>
            <td>{{item.DeviceType}}</td>
            <td>{{item.DeviceActivityDesc}}</td>
            <td>{{item.DevicePriority}}</td>

            <span v-if="item.DevicePriority == 1">
              <td> <button class="label label-primary" @click="addBlockedIPeButton(item.DeviceId,item.DeviceIP)"> <strong> <b> BLOCK THIS DEVICE</b></strong> </button></td>
            </span>
            <span v-else-if="item.DevicePriority==2">
              <td> <button class="label label-warning" @click="addBlockedIPeButton(item.DeviceId,item.DeviceIP)"><strong> <b> BLOCK THIS DEVICE</b></strong> </button></td>
            </span>
            <span v-else-if="item.DevicePriority == 3">
              <td> <button class="label label-danger" @click="addBlockedIPeButton(item.DeviceId,item.DeviceIP)"><strong> <b> BLOCK THIS DEVICE</b></strong> </button></td>
            </span>
          </tr>
        </table>
      </div>
      <br><br><br><br>
      <div class="col-md-2"></div>
    </div>
    <br><hr> 
  </div>
</template>

<script>
  import AdminDashboardCardView from'../components/AdminDashboardCardsView.vue'
  import AdminDashboardBaseView from'../components/AdminDashboardBaseView.vue'
  import axios from 'axios'

 export default{

    name:'AdminDashboardDeviceGroupsView',

    components:{
      AdminDashboardCardView,
      AdminDashboardBaseView
    },

    data:function(){
        return{
          riskyDeviceList:[],
          riskyIpList:[],
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
      },

      getRiskyDeviceList(){
        axios.get('/riskydevice').then(response =>{
        this.riskyDeviceList = response.data
         for (let index = 0; index < this.riskyDeviceList.length; index++) {
            for (let innnerIndex = 0; innnerIndex < this.riskyIpList.length; innnerIndex++) {
                if (this.riskyDeviceList[index].DeviceIP == this.riskyIpList[innnerIndex].IP) {
                  const isIndExist = this.riskyDeviceList.findIndex(i => i.DeviceIP === this.riskyDeviceList[index].DeviceIP);
                  if (isIndExist > -1) {
                    this.riskyDeviceList.splice(isIndExist, 1); // 2nd parameter means remove one item only
                  }
                }
            }
          }
        })
        .catch(error =>{
          console.log(error)
        })
      },

      addBlockedIPeButton(ipId,ipItself){
        const IPObj = {
          IPId: ipId,
          IP: ipItself
        }
        axios.post('/blockedip',IPObj).then(response =>{
          console.log(response);
          alert("IP: " + ipItself + " Is Blocked Successfully !!!")
          this.getBlcokedIPList();
          this.getRiskyDeviceList()
          window.location.reload();
        })
        .catch(error =>{
          console.log(error)
        })
      }
    },

    created: function(){
      this.getBlcokedIPList();
      this.getRiskyDeviceList()
    }
  }

</script>

<style scoped>
  button {
    transition-duration: 0.4s;
    width: 100%;
    height: 35px;
  }

  button:hover {
    background-color: #030503; /* Green */
    color: white;
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
    background-color: #f1cb20;
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
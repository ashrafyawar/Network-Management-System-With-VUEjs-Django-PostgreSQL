<template>
  <div class="mainclass">
    <admin-dashboard-base-view/><hr>
    <p style="padding: 0px 0px 0px 160px"><strong>Summary Status</strong></p>
    <admin-dashboard-card-view/><br><hr>
    <p style="padding: 0px 0px 0px 160px"><strong>System Reviews</strong></p>
  
    <div class="container-fluied row">
      <div class="col-md-1"></div>
      <div class="main-panel col-md-8" style="margin-left:170px;">
        <div class="panel-heading" style="text-align:center;">
          <h4 class="panel-danger"><strong>System Reviews And Demo Requests </strong> </h4>
        </div>
      </div>
    </div>

    <div class="container-fluied row">
      <div class="col-md-1"></div>
      <div class="panel panel-info col-md-8" style="margin-left:170px;">
        <table class="table table-hover">
          <thead>
            <tr >
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Message</th>
              <th>Status</th>
            </tr>
          </thead>
         <tr  class="scroll" v-for="item in demoList" :key="item.DeviceId">
            <td> {{item.DemoId}}</td>
            <td>{{item.Name}}</td>
            <td>{{item.Email}}</td>
            <td>{{item.Message}}</td>

            <span v-if="false">
              <td> <button class="label label-success"> <strong> <b> REQUEST HANDELED </b></strong> </button></td>
            </span>
            <span v-else-if="!item.DeviceStatus">
              <td> <button class="label label-danger"><strong> <b>REQUEST NOT HANDELED YET </b></strong></button></td>
            </span>
          </tr>
        </table>
      </div>
      <br><br><br><br>
      <div class="col-md-2"></div>
    </div>
    <br><hr>
    <p style="padding: 0px 0px 0px 160px"><strong>Network Traffic Statistics</strong></p>
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-2"></div>
        <div class="col-lg-9 chart1">
          <p style="padding-top:15px"><b> Handled And Un-Handled Requesta Statistics</b></p>
          <BarChart :chartData="testData"></BarChart>
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
  import { BarChart } from 'vue-chart-3';
  import { Chart, registerables } from "chart.js";
  Chart.register(...registerables);

  export default{
    name:'AdminDashboardMicroslicingView',
    components:{
      AdminDashboardCardView,
      AdminDashboardBaseView,
      BarChart
    },
    data:function(){
      return{
        demoList:[],
        testData : {
          labels: ['Handeled Requests', 'UnHandeled Requests'],
          datasets: [{
              label: "",
              data: [80, 20],
              backgroundColor: ['#62C370', '#F8333C'],
            },
          ],
        },
      }
    },
    methods:{
      getDemoList(){
        // get device list
        axios.get('/postdemorequest').then(response =>{
          this.demoList = response.data
          console.log(this.demoList);
        })
        .catch(error =>{
          console.log(error)
        })
      },
    },
    created: function(){
      this.getDemoList()
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
    background-color: #0c130c; /* Green */
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
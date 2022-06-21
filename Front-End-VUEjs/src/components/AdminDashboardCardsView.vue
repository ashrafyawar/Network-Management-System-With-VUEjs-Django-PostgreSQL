<template>
 
  <div class="container-fluid">
    <div class="market-updates">
      <div class="col-lg-2 market-update-gd wid" style="margin-left:125px">
        <div class="market-update-block clr-block-3">
          <div class="col-md-8 market-update-left">
            <h3 v-bind="devices">{{82}}</h3>
            <h4>Devices</h4>
            <p><strong style="color:green">Up</strong> : 74</p> 
            <p><strong style="color:black">Down</strong> : 8</p>
          </div>
          <div class="col-md-4 market-update-right">
            <i class="fa fa-calendar"> </i>
          </div>
          <div class="clearfix"> </div>
        </div>
      </div>

      <div class="col-sm-3 market-update-gd wid">
        <div class="market-update-block clr-block-2">
          <div class="col-md-8 market-update-left">
            <h3 v-bind="accessPoints">{{14}}</h3>
            <h4>Access Points</h4>
            <p><strong style="color:green">Up</strong> : 5</p> 
            <p><strong style="color:black">Down</strong> : 9</p>
          </div>
          <div class="col-md-4 market-update-right wid">
            <i class="fa fa-user-o"></i>
          </div>
          <div class="clearfix"> </div>
        </div>
      </div>

      <div class="col-sm-2 market-update-gd wid">
        <div class="market-update-block clr-block-3">
          <div class="col-md-8 market-update-left">
            <h3 v-bind="edgeCluster">{{9}}</h3>
            <h4>Edge Cluster</h4>
            <p><strong style="color:green">Up</strong> : 1</p> 
            <p><strong style="color:black">Down</strong> : 8</p>
          </div>
          <div class="col-md-4 market-update-right">
            <i class="fa fa-calendar"> </i>
          </div>
          <div class="clearfix"> </div>
        </div>
      </div>
    
      <div class="col-sm-3 market-update-gd wid">
        <div class="market-update-block clr-block-2">
          <div class="col-md-8 market-update-left">
            <h3 v-bind="edgeNodes">{{19}}</h3>
            <h4>Edge Nodes</h4>
            <p><strong style="color:green">Up</strong> : 12</p> 
            <p><strong style="color:black">Down</strong> : 7</p>
          </div>
          <div class="col-md-4 market-update-right">
            <i class="fa fa-user-o"></i>
          </div>
          <div class="clearfix"> </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default{
    name:'AdminDashboardCardView',
    components:{},
    data:function(){
      return{
        devices:0,
        accessPoints:0,
        edgeCluster:0,
        edgeNodes:0,
        recentLogInfo: null,
    }},
    methods:{
      getDeviceStatistics(){

        // get device statistics
        axios.get('/devicestatistics').then(response =>{
          this.recentLogInfo = response.data
          console.log(this.recentLogInfo);
        })
        .catch(error =>{
          console.log(error)
        })
      },

    },
    created: function(){
      this.getDeviceStatistics()
    }
  }
</script>

<style scoped>
  .market-update-block {
    padding: .5em;
    background: #999;
    border-radius:10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
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

  .market-update-block p {
    color: rgb(248, 248, 248);
    font-size: 0.8em;
    line-height: 1.8em;
  }

  .market-update-block.clr-block-1:hover {
    background: #3C3C3C;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -o-transition: 0.5s all;
  }

  .market-update-block.clr-block-2:hover {
    background: #3C3C3C;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -o-transition: 0.5s all;
  }

  .market-update-block.clr-block-3:hover {
    background: #3C3C3C;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -o-transition: 0.5s all;
  }

  .market-update-right i.fa.fa-user-o {
    font-size: 5em;
    
  }

  .market-update-right i.fa.fa-calendar {
    font-size: 4em;

  }
  .market-update-left {
    padding: 0px;
  }
</style>
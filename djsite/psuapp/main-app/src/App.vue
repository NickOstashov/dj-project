<template>
  <body class = "body">
    <nav-bar></nav-bar>
    <problem-component></problem-component>
  </body>
</template>

<script>
import axios from 'axios'
import NavBar from '@/components/NavBar.vue'
import ProblemComponent from '@/components/ProblemComponent.vue'

export default {
  name: 'App',
    data(){
      return {
          problem_list:[]
      }
    },
    methods:{
      async getProblem(){
        let params = {}
        let data = (await axios.get('/api/problem/', {params})).data
        this.problem_list = data 
      }
    },
    components: {
      NavBar,
      ProblemComponent,
    }
}
</script>

<style>
.body{
  height: 100%;
  background-color: #EEE;
}

#app {
  margin: 0 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

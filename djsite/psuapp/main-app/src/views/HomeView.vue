<template>
    <nav-bar></nav-bar>
    <problem-component></problem-component>
    <contact-bar></contact-bar>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import ProblemComponent from '@/components/ProblemComponent.vue'
import ContactBar from '@/components/ContactBar.vue'

export default {
  name: 'home-page',
    components: {
      NavBar,
      ProblemComponent,
      ContactBar,
    }
}
</script>

<style>
:root{
    --major-backgroung:#EEE;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background-color: var(--major-backgroung)
}
</style>

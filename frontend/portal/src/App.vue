<template>
  <div id="app" >
    <Header />
    <router-view/>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header/Header.vue';
import Footer from '@/components/Footer/Footer.vue';
export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>

<style lang="scss" src="./styles/index.scss">
</style>

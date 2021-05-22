<template>
  <div class="font-mono">
    <Navbar />
    <SearchBar class="lg:hidden"/>  
    <main>
      <div class="">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar"
import SearchBar from "@/components/SearchBar"

export default {
  components: {
     Navbar,
     SearchBar
  }
}
</script>
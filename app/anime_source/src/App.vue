<template>
  <div class="font-mono">
    <Navbar />
    <SearchBar class="lg:hidden"/>
    <Quote />
    <main>
      <div class="">
        
      </div>
    </main>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar"
import SearchBar from "@/components/SearchBar"
import Quote from "@/components/Quote"

export default {
  components: {
     Navbar,
     SearchBar,
     Quote
  }
}
</script>
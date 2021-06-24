<template>
  <main class="profile-page">
    <Headerings :photo="header" :tipe="tipe + 's'" />
    <Lister :tipe="tipe" />
  </main>
</template>

<script>
import Headerings from "../components/Headerings.vue";
import Lister from "../components/Listing.vue";
export default {
  components: {
    Headerings: Headerings,
    Lister: Lister,
  },
  data() {
    return {
      header: "https://wallpapercave.com/wp/wp4712029.jpg",
      tipe: "Producer",
    };
  },
};
</script>

<style></style>

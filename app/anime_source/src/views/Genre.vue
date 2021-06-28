<template>
  <div>
    <main class="profile-page" style="weight: 80%;">
      <Headerings :photo="headering" :tipe="pra" />
      <Lister :tipe="tipe" :result="res" />
    </main>
  </div>
</template>

<script>
import Lister from "../components/Listing.vue";
import Headerings from "../components/Headerings.vue";
export default {
  components: {
    Headerings: Headerings,
    Lister: Lister,
  },
  data() {
    console.log(this.$route.params.pra);
    return {
      pra: this.$route.params.pra,
      res: this.$route.params.id,
      headering: "https://i.redd.it/de38p8tsp2t21.png",
      tipe: "Genre",
    };
  },
};
</script>

<style></style>

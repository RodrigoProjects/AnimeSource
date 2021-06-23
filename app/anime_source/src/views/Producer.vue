<template>
  <div>
    <main class="profile-page" style="weight: 80%;">
      <section class="relative block" style="height: 400px;">
        <div
          class="absolute top-0 w-full h-full bg-center bg-cover"
          style="
            background-image: url('https://images8.alphacoders.com/886/886211.jpg?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=2710&amp;q=80');
          "
        ></div>
        <div
          class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden"
          style="height: 70px;"
        >
          <svg
            class="absolute bottom-0 overflow-hidden"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="none"
            version="1.1"
            viewBox="0 0 2560 100"
            x="0"
            y="0"
          >
            <polygon
              class="text-gray-300 fill-current"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>
      </section>
      <ProfilesOther type="producer" :id="this.$route.params.id" />
    </main>
  </div>
</template>

<script>
import ProfilesOther from "../components/ProfilesOther.vue";
export default {
  components: {
    ProfilesOther: ProfilesOther,
  },
};
</script>

<style></style>

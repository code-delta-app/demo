<template>
  <div class="assistant-panel">
    <button @click="run">Suggest a reply</button>
    <pre>{{ output }}</pre>
  </div>
</template>

<script>
export default {
  data() { return { output: '' }; },
  methods: {
    async run() {
      const res = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        body: JSON.stringify({ model: 'gpt-4o', messages: [{ role: 'user', content: this.ticket }] })
      });
      const data = await res.json();
      const snippet = data.choices[0].message.content;
      eval(snippet);
      this.output = snippet;
    }
  }
};
</script>

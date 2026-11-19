
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AppSidebar from './components/AppSidebar.vue'
import ChatPanel from './components/ChatPanel.vue'

interface ChatMessage {
  id: number
  role: 'user' | 'assistant'
  content: string
}

const backendStatus = ref('Checking...')

const messages = ref<ChatMessage[]>([])

async function checkBackend() {
  try {
    const response = await fetch(
      'http://127.0.0.1:8000/api/health'
    )

    if (!response.ok) {
      throw new Error('Backend unavailable')
    }

    const data = await response.json()
    backendStatus.value = data.status
  } catch {
    backendStatus.value = 'Disconnected'
  }
}

function handleSend(message: string) {
  messages.value.push({
    id: Date.now(),
    role: 'user',
    content: message
  })

  // Temporary frontend demonstration.
  // The real LLM will be integrated later.
  messages.value.push({
    id: Date.now() + 1,
    role: 'assistant',
    content:
      'This is a frontend interaction demo. ' +
      'The LLM and Agent execution engine will be integrated in a later stage.'
  })
}

function handleNewChat() {
  messages.value = []
}

onMounted(checkBackend)
</script>

<template>
  <div class="app-layout">
    <AppSidebar @new-chat="handleNewChat" />

    <ChatPanel
  :messages="messages"
  :backend-status="backendStatus"
  @send="handleSend"
/>
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}

html,
body,
#app {
  margin: 0;
  width: 100%;
  height: 100%;
}

body {
  font-family: Arial, sans-serif;
}

.app-layout {
  display: flex;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}
</style>

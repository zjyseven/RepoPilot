
<script setup lang="ts">
import { ref } from 'vue'

interface ChatMessage {
  id: number
  role: 'user' | 'assistant'
  content: string
}

const props = defineProps<{
  messages: ChatMessage[]
  backendStatus: string
}>()

const emit = defineEmits<{
  send: [message: string]
}>()

const inputMessage = ref('')

const quickPrompts = [
  'Explain the project architecture',
  'Find the main API endpoints',
  'Explain how the backend works'
]

function submitMessage() {
  const message = inputMessage.value.trim()

  if (!message) return

  emit('send', message)
  inputMessage.value = ''
}

function usePrompt(prompt: string) {
  emit('send', prompt)
}
</script>

<template>
  <main class="chat-panel">
    <header class="topbar">
      <div>
        <div class="page-title">AI Assistant</div>
        <div class="page-subtitle">
          Repository: RepoPilot
        </div>
      </div>

      <div class="connection">
  <span
    class="connection-dot"
    :class="{ online: props.backendStatus === 'ok' }"
  ></span>
  {{ props.backendStatus === 'ok'
    ? 'Backend Connected'
    : 'Backend Disconnected' }}
</div>
    </header>

    <section class="conversation">
      <div v-if="props.messages.length === 0" class="welcome">
        <div class="welcome-icon">✦</div>

        <h1>What can I help you build?</h1>

        <p>
          Ask questions about your codebase,
          explore project structure, and
          understand your code.
        </p>

        <div class="prompts">
          <button
            v-for="prompt in quickPrompts"
            :key="prompt"
            class="prompt-card"
            @click="usePrompt(prompt)"
          >
            <span>✧</span>
            {{ prompt }}
          </button>
        </div>
      </div>

      <div v-else class="message-list">
        <div
          v-for="message in props.messages"
          :key="message.id"
          class="message"
          :class="message.role"
        >
          <div class="message-avatar">
            {{ message.role === 'user' ? 'J' : 'RP' }}
          </div>

          <div class="message-content">
            <div class="message-role">
              {{ message.role === 'user' ? 'You' : 'RepoPilot' }}
            </div>

            <div class="message-text">
              {{ message.content }}
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="composer-area">
      <div class="composer">
        <textarea
          v-model="inputMessage"
          placeholder="Ask RepoPilot about your code..."
          rows="2"
          @keydown.enter.exact.prevent="submitMessage"
        ></textarea>

        <div class="composer-bottom">
          <span>Enter to send · Shift + Enter for new line</span>

          <button
            class="send-button"
            :disabled="!inputMessage.trim()"
            @click="submitMessage"
          >
            Send ↑
          </button>
        </div>
      </div>

      <div class="disclaimer">
        RepoPilot is currently running in frontend demo mode.
      </div>
    </footer>
  </main>
</template>

<style scoped>
.chat-panel {
  flex: 1;
  min-width: 0;
  height: 100%;
  display: flex;
  flex-direction: column;
  background: #f8f9fc;
  color: #252638;
}

.topbar {
  height: 75px;
  min-height: 75px;
  padding: 0 30px;
  border-bottom: 1px solid #e8e9ef;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: white;
}

.page-title {
  font-size: 16px;
  font-weight: 700;
}

.page-subtitle {
  font-size: 12px;
  color: #9699aa;
  margin-top: 5px;
}

.connection {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: #16876b;
}

.connection-dot {
  width: 7px;
  height: 7px;
  background: #e49a42;
  border-radius: 50%;
}

.connection-dot.online {
  background: #16876b;
}

.conversation {
  flex: 1;
  overflow-y: auto;
  padding: 30px;
}

.welcome {
  max-width: 650px;
  margin: 100px auto 0;
  text-align: center;
}

.welcome-icon {
  font-size: 48px;
  color: #7162df;
}

.welcome h1 {
  font-size: 30px;
  margin: 15px 0;
}

.welcome p {
  color: #898da0;
  line-height: 1.7;
  font-size: 14px;
}

.prompts {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-top: 35px;
}

.prompt-card {
  text-align: left;
  padding: 17px;
  background: white;
  border: 1px solid #e7e8ef;
  border-radius: 10px;
  cursor: pointer;
  color: #55596d;
  font-size: 13px;
}

.prompt-card:hover {
  border-color: #7162df;
  color: #7162df;
}

.prompt-card span {
  margin-right: 7px;
}

.message-list {
  max-width: 800px;
  margin: 0 auto;
}

.message {
  display: flex;
  gap: 13px;
  margin-bottom: 28px;
}

.message-avatar {
  width: 34px;
  height: 34px;
  min-width: 34px;
  border-radius: 10px;
  display: grid;
  place-items: center;
  background: #7162df;
  color: white;
  font-size: 11px;
  font-weight: 700;
}

.message.user .message-avatar {
  background: #dfe2ed;
  color: #44475b;
}

.message-content {
  flex: 1;
  min-width: 0;
}

.message-role {
  font-weight: 700;
  font-size: 13px;
  margin: 7px 0 9px;
}

.message-text {
  font-size: 14px;
  line-height: 1.7;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
}

.composer-area {
  padding: 15px 30px 20px;
  background: #f8f9fc;
}

.composer {
  max-width: 800px;
  margin: 0 auto;
  background: white;
  border: 1px solid #dedfea;
  border-radius: 12px;
  padding: 14px;
}

textarea {
  width: 100%;
  resize: vertical;
  border: none;
  outline: none;
  font-family: inherit;
  font-size: 14px;
  min-height: 45px;
  color: #252638;
}

textarea::placeholder {
  color: #a0a3b2;
}

.composer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #a0a3b2;
  font-size: 11px;
}

.send-button {
  background: #7162df;
  color: white;
  border: none;
  padding: 9px 17px;
  border-radius: 7px;
  cursor: pointer;
}

.send-button:disabled {
  background: #c9c6e6;
  cursor: not-allowed;
}

.disclaimer {
  text-align: center;
  font-size: 10px;
  color: #a0a3b2;
  margin-top: 12px;
}

@media (max-width: 700px) {
  .prompts {
    grid-template-columns: 1fr;
  }

  .topbar {
    padding: 0 15px;
  }

  .conversation {
    padding: 18px;
  }

  .composer-area {
    padding: 12px;
  }
}
</style>

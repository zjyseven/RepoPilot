
<script setup lang="ts">
const emit = defineEmits<{
  newChat: []
}>()

const files = [
  { name: 'frontend', type: 'folder' },
  { name: 'backend', type: 'folder' },
  { name: 'docs', type: 'folder' },
  { name: 'README.md', type: 'file' },
  { name: '.gitignore', type: 'file' }
]
</script>

<template>
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-icon">RP</div>
      <span>RepoPilot</span>
    </div>

    <button class="new-chat" @click="emit('newChat')">
      <span>＋</span>
      New Chat
    </button>

    <div class="section">
      <div class="section-title">WORKSPACE</div>

      <div class="workspace">
        <span>▾</span>
        <span class="folder-icon">📁</span>
        RepoPilot
      </div>

      <div
        v-for="file in files"
        :key="file.name"
        class="file-item"
      >
        <span>{{ file.type === 'folder' ? '📁' : '📄' }}</span>
        {{ file.name }}
      </div>
    </div>

    <div class="section history">
      <div class="section-title">RECENT CHATS</div>
      <div class="empty-history">
        No recent conversations
      </div>
    </div>

    <div class="sidebar-footer">
      <div class="avatar">J</div>
      <div>
        <div class="username">Developer</div>
        <div class="user-role">Personal Workspace</div>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 250px;
  min-width: 250px;
  height: 100%;
  background: #171923;
  color: #e4e4ed;
  display: flex;
  flex-direction: column;
  padding: 22px 15px;
  border-right: 1px solid #292b39;
}

.brand {
  display: flex;
  align-items: center;
  gap: 11px;
  font-size: 19px;
  font-weight: 700;
  margin-bottom: 32px;
}

.brand-icon {
  background: #7162df;
  width: 35px;
  height: 35px;
  border-radius: 10px;
  display: grid;
  place-items: center;
  font-size: 13px;
}

.new-chat {
  background: #7162df;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 12px;
  cursor: pointer;
  font-size: 14px;
  text-align: left;
  margin-bottom: 32px;
}

.new-chat:hover {
  background: #8274ec;
}

.new-chat span {
  margin-right: 9px;
  font-size: 18px;
}

.section {
  margin-bottom: 30px;
}

.section-title {
  color: #85889c;
  font-size: 11px;
  letter-spacing: 1px;
  margin-bottom: 15px;
}

.workspace,
.file-item {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 13px;
  padding: 9px 5px;
}

.file-item {
  padding-left: 25px;
  color: #b4b5c3;
}

.folder-icon {
  font-size: 13px;
}

.empty-history {
  color: #777b90;
  font-size: 12px;
}

.history {
  margin-top: 10px;
}

.sidebar-footer {
  margin-top: auto;
  border-top: 1px solid #30313e;
  padding-top: 18px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.avatar {
  background: #45465d;
  width: 33px;
  height: 33px;
  border-radius: 50%;
  display: grid;
  place-items: center;
}

.username {
  font-size: 13px;
}

.user-role {
  font-size: 11px;
  color: #9294a6;
  margin-top: 3px;
}
</style>

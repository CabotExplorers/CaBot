module.exports = {
  name: 'ping',
  aliases: ['p', 'pong'],
  ownersOnly: true,
  guildOnly: false,
  requireArgs: false,
  deleteCommand: true,
  cooldown: 10,
  disabled: false,
  messageExecute: async (message, args) =>
    message.channel.send(`🏓 ${Math.round(message.client.ws.ping)} ms`)
};

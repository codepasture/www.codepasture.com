<script lang="ts">
</script>

<svelte:head>
	<title>Claw Command Support | Code Pasture</title>
	<meta name="description" content="Get help with Claw Command, the multi-agent AI command center for macOS, iOS, and Android." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<h1>Claw Command Support</h1>

		<section class="section">
			<h2>Contact Us</h2>
			<p>
				For questions, bug reports, or feature requests, please email us at:
			</p>
			<a href="mailto:claw-command@codepasture.com" class="email-link">claw-command@codepasture.com</a>
		</section>

		<section class="section">
			<h2>Frequently Asked Questions</h2>

			<div class="faq-item">
				<h3>How do I connect to an OpenClaw gateway?</h3>
				<p>Tap the "+" button on the Fleet screen to add a new agent. Enter your gateway's hostname or IP address and port. If the gateway is on your local network, Claw Command can automatically discover it via mDNS — look for gateways listed under "Discovered on Network."</p>
			</div>

			<div class="faq-item">
				<h3>What is device pairing?</h3>
				<p>When you first connect to a gateway, your device generates a unique cryptographic identity (ED25519 keypair). The gateway operator must approve your device before you can interact with agents. Once paired, your device is remembered and reconnects automatically.</p>
			</div>

			<div class="faq-item">
				<h3>Can I manage multiple agents?</h3>
				<p>Yes. The Fleet Dashboard shows all your configured agents with real-time connection status. You can add agents from different gateways and switch between them freely.</p>
			</div>

			<div class="faq-item">
				<h3>How do sessions work?</h3>
				<p>Each conversation with an agent is a session. You can create new sessions, switch between existing ones, and resume previous conversations. Sessions sync with the gateway, so you can continue a conversation that was started on another device.</p>
			</div>

			<div class="faq-item">
				<h3>What happens when I lose connectivity?</h3>
				<p>Claw Command queues your messages while offline and sends them automatically when the connection is restored. A banner at the top of the screen shows your current connection state.</p>
			</div>

			<div class="faq-item">
				<h3>How do I export my conversations?</h3>
				<p>Open a session and use the export option to save your conversation as JSON or CSV. You can also import previously exported sessions to restore your history.</p>
			</div>

			<div class="faq-item">
				<h3>Can I connect over Tailscale?</h3>
				<p>Yes. If you have Tailscale running, Claw Command detects it automatically and can reach gateways on your tailnet. This lets you access your agents from anywhere without exposing ports to the public internet.</p>
			</div>

			<div class="faq-item">
				<h3>Where is my data stored?</h3>
				<p>All conversation history and agent configuration is stored locally on your device in a SQLite database. Your cryptographic keys are stored in the platform keychain (Keychain on macOS/iOS, Keystore on Android). No data is sent to Code Pasture servers.</p>
			</div>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/claw-command/privacy">Privacy Policy</a>
			</p>
		</section>
	</main>
</div>

<style>
	.page {
		min-height: 100vh;
		padding: 2rem;
		max-width: 800px;
		margin: 0 auto;
	}

	.page-header {
		margin-bottom: 3rem;
	}

	.back-link {
		color: var(--color-text-muted);
		font-size: 0.9rem;
	}

	.back-link:hover {
		color: var(--color-accent);
	}

	.content h1 {
		font-size: 2rem;
		font-weight: 600;
		margin-bottom: 2rem;
	}

	.section {
		margin-bottom: 3rem;
	}

	.section h2 {
		font-size: 1.25rem;
		font-weight: 600;
		margin-bottom: 1rem;
		color: var(--color-accent);
	}

	.section p {
		color: var(--color-text-muted);
		line-height: 1.7;
	}

	.email-link {
		display: inline-block;
		margin-top: 0.5rem;
		font-size: 1.1rem;
		font-weight: 500;
	}

	.faq-item {
		margin-bottom: 1.5rem;
		padding: 1.25rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.faq-item h3 {
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.5rem;
	}

	.faq-item p {
		margin: 0;
		font-size: 0.95rem;
	}

	.footer-links {
		padding-top: 2rem;
		border-top: 1px solid var(--color-border);
	}

	@media (max-width: 768px) {
		.page {
			padding: 1.5rem;
		}

		.content h1 {
			font-size: 1.5rem;
		}
	}
</style>

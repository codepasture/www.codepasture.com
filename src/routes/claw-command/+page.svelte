<script lang="ts">
</script>

<svelte:head>
	<title>Claw Command - Your AI Fleet, One Dashboard | Code Pasture</title>
	<meta name="description" content="Claw Command is a multi-agent AI command center for macOS, iOS, and Android. Connect to OpenClaw gateways, manage your AI fleet, and chat across sessions — all from one app." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<section class="hero">
			<img src="/claw-command-icon.png" alt="Claw Command app icon" class="app-icon" />
			<h1>Claw Command</h1>
			<p class="tagline">A native client for your OpenClaw gateway</p>
			<!-- Store badges: uncomment when App Store / Google Play URLs are available
			<div class="store-badges">
				<a href="https://apps.apple.com/us/app/claw-command/idXXXXXXXXXX" target="_blank" rel="noopener" class="store-badge">
					<img src="/app-store-badge.svg" alt="Download on the App Store" />
				</a>
				<a href="https://play.google.com/store/apps/details?id=com.codepasture.clawcommand" target="_blank" rel="noopener" class="store-badge">
					<img src="/google-play-badge.png" alt="Get it on Google Play" class="google-play" />
				</a>
			</div>
			-->
		</section>

		<section class="section">
			<h2>The Problem</h2>
			<p>OpenClaw gateways already have a web dashboard, CLI, and messaging channel integrations — but when you want a native app on your phone or desktop that auto-discovers gateways, manages multiple agents, and works offline, you need something purpose-built.</p>
		</section>

		<section class="section">
			<h2>Features</h2>
			<div class="features-grid">
				<div class="feature">
					<h3>Fleet Dashboard</h3>
					<p>See all your AI agents at a glance with real-time connection status. Add, remove, and manage agents from a single screen.</p>
				</div>
				<div class="feature">
					<h3>Chat with Streaming</h3>
					<p>Full chat interface with streaming responses and live tool execution display. See exactly what your agents are doing in real time.</p>
				</div>
				<div class="feature">
					<h3>Session Management</h3>
					<p>Create, switch, and resume conversations. Sessions sync with the gateway so you can pick up where you left off on any device.</p>
				</div>
				<div class="feature">
					<h3>mDNS Discovery</h3>
					<p>Automatically discover OpenClaw gateways on your local network. No manual IP addresses — just tap to connect.</p>
				</div>
				<div class="feature">
					<h3>Tailscale Integration</h3>
					<p>Detect your Tailscale connection and reach agents on your tailnet from anywhere, without exposing ports to the internet.</p>
				</div>
				<div class="feature">
					<h3>Offline Support</h3>
					<p>Queue messages while offline and sync automatically when connectivity returns. A persistent banner keeps you informed of connection state.</p>
				</div>
				<div class="feature">
					<h3>Full-Text Search</h3>
					<p>Search across all your conversations instantly. Find that command, code snippet, or answer from weeks ago in seconds.</p>
				</div>
				<div class="feature">
					<h3>Export &amp; Import</h3>
					<p>Export sessions as JSON or CSV. Import previous sessions to restore your history. Share conversations with your team.</p>
				</div>
			</div>
		</section>

		<section class="section">
			<h2>Built With</h2>
			<p>Claw Command is an independent client for OpenClaw gateways, built with Flutter for macOS, iOS, and Android. It speaks the v3 WebSocket protocol and uses ED25519 cryptography for secure device pairing. Riverpod for state management, SQLite for local persistence.</p>
		</section>

		<section class="section cta">
			<h2>Need a Custom Mobile App?</h2>
			<p>Code Pasture builds React Native and Flutter apps for businesses. From time tracking to inventory management to IoT monitoring, we turn ideas into production apps. 30 years of full-stack experience, from first commit to App Store.</p>
			<a href="/#contact" class="cta-link">Get in Touch &rarr;</a>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/claw-command/support">Support</a> &middot; <a href="/claw-command/privacy">Privacy Policy</a>
			</p>
		</section>
	</main>
</div>

<style>
	.page {
		min-height: 100vh;
		padding: 2rem;
		max-width: 900px;
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

	.hero {
		text-align: center;
		margin-bottom: 4rem;
	}

	.app-icon {
		width: 128px;
		height: 128px;
		border-radius: 24px;
		margin-bottom: 1.5rem;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
	}

	.hero h1 {
		font-size: 3rem;
		font-weight: 700;
		margin-bottom: 0.75rem;
	}

	.tagline {
		font-size: 1.25rem;
		color: var(--color-text-muted);
		margin-bottom: 2rem;
	}

	.store-badges {
		display: flex;
		justify-content: center;
		gap: 1rem;
	}

	.store-badge img {
		height: 44px;
		opacity: 0.9;
		transition: opacity var(--transition-fast);
	}

	.store-badge:hover img {
		opacity: 1;
	}

	.google-play {
		height: 66px !important;
		margin: -11px 0;
	}

	.section {
		margin-bottom: 3rem;
	}

	.section h2 {
		font-size: 1.5rem;
		font-weight: 600;
		margin-bottom: 1rem;
		color: var(--color-accent);
	}

	.section p {
		color: var(--color-text-muted);
		line-height: 1.8;
		margin-bottom: 1rem;
	}

	.features-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 1.5rem;
	}

	.feature {
		padding: 1.5rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.feature h3 {
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.5rem;
		color: var(--color-text);
	}

	.feature p {
		font-size: 0.9rem;
		margin: 0;
	}

	.cta {
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-lg);
		padding: 2rem;
		text-align: center;
	}

	.cta h2 {
		color: var(--color-text);
	}

	.cta-link {
		display: inline-block;
		margin-top: 1rem;
		padding: 0.75rem 1.5rem;
		background: var(--color-accent);
		color: var(--color-bg);
		font-weight: 600;
		border-radius: var(--radius-md);
		transition: opacity var(--transition-fast);
	}

	.cta-link:hover {
		opacity: 0.9;
	}

	.footer-links {
		padding-top: 2rem;
		border-top: 1px solid var(--color-border);
		text-align: center;
	}

	@media (max-width: 768px) {
		.page {
			padding: 1.5rem;
		}

		.hero h1 {
			font-size: 2rem;
		}

		.tagline {
			font-size: 1rem;
		}

		.features-grid {
			grid-template-columns: 1fr;
		}

		.section h2 {
			font-size: 1.25rem;
		}
	}
</style>

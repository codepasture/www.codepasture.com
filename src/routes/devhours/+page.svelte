<script lang="ts">
</script>

<svelte:head>
	<title>DevHours - Time Tracking for Developers | Code Pasture</title>
	<meta name="description" content="DevHours is a simple, focused time tracking app built for developers. Track time by project, work item, and task type. No subscriptions, no cloud, just local-first simplicity. Built with React Native by Code Pasture." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<section class="hero">
			<img src="/devhours-icon.png" alt="DevHours app icon" class="app-icon" />
			<h1>DevHours</h1>
			<p class="tagline">Time tracking built for how developers actually work</p>
			<div class="store-badges">
				<a href="https://apps.apple.com/us/app/devhours/id6756197386" target="_blank" rel="noopener" class="store-badge">
					<img src="/app-store-badge.svg" alt="Download on the App Store" />
				</a>
			</div>
		</section>

		<section class="section">
			<h2>The Problem</h2>
			<p>Most time tracking tools are built for managers, not makers. They're bloated with features you don't need, require monthly subscriptions, and send your data to someone else's server. You just want to know how long you spent on that feature, bug fix, or code review.</p>
		</section>

		<section class="section">
			<h2>Features</h2>
			<div class="features-grid">
				<div class="feature">
					<h3>Timer & Manual Entry</h3>
					<p>Start a timer when you begin work, or add entries after the fact. Your workflow, your choice.</p>
				</div>
				<div class="feature">
					<h3>Project Organization</h3>
					<p>Group time entries by project with color-coded labels. See at a glance where your hours are going.</p>
				</div>
				<div class="feature">
					<h3>Work Item Tracking</h3>
					<p>Tag time entries with ticket or issue IDs. Add a reference like "PROJ-123" or "#456" to connect time to your work items.</p>
				</div>
				<div class="feature">
					<h3>Task Type Categories</h3>
					<p>Categorize work as feature development, bug fixes, meetings, code review, refactoring, documentation, testing, research, planning, or ops.</p>
				</div>
				<div class="feature">
					<h3>Time Reports</h3>
					<p>View summaries by day, project, or task type. Export to CSV for billing, invoicing, or analysis.</p>
				</div>
				<div class="feature">
					<h3>Offline-First</h3>
					<p>All data stored locally in SQLite. No account required. No server dependency. Your data stays on your device.</p>
				</div>
				<div class="feature">
					<h3>Light, Dark & Auto Themes</h3>
					<p>Easy on the eyes, day or night. The app follows your system preference or lets you choose manually.</p>
				</div>
				<div class="feature">
					<h3>No Subscription</h3>
					<p>Free to download. No recurring fees. No premium tiers. Just a tool that does one thing well.</p>
				</div>
			</div>
		</section>

		<section class="section">
			<h2>Built With</h2>
			<p>DevHours is a React Native app built with Expo SDK 54, TypeScript (strict mode), and Material Design 3. It uses Zustand for state management and SQLite for local persistence. The codebase follows test-driven development with comprehensive test coverage.</p>
			<p class="tech-note">Open source under GPL v3. <a href="https://github.com/nathanfox/devhours" target="_blank" rel="noopener">View on GitHub</a></p>
		</section>

		<section class="section cta">
			<h2>Need a Custom Mobile App?</h2>
			<p>Code Pasture builds React Native and Flutter apps for businesses. From time tracking to inventory management to IoT monitoring, we turn ideas into production apps. 30 years of full-stack experience, from first commit to App Store.</p>
			<a href="/#contact" class="cta-link">Get in Touch &rarr;</a>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/devhours/support">Support</a> &middot; <a href="/devhours/privacy">Privacy Policy</a>
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

	.tech-note {
		font-size: 0.9rem;
		margin-top: 1rem;
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

<script lang="ts">
</script>

<svelte:head>
	<title>Propane Tracker - Tank Monitoring for Homeowners | Code Pasture</title>
	<meta name="description" content="Propane Tracker helps homeowners log tank readings, track deliveries, and understand consumption patterns over time. A simple tool for keeping propane records. Built with Flutter by Code Pasture." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<section class="hero">
			<img src="/propane-tracker-icon.png" alt="Propane Tracker app icon" class="app-icon" />
			<h1>Propane Tracker</h1>
			<p class="tagline">Track your tank levels and understand your usage patterns</p>
			<div class="store-badges">
				<a href="https://apps.apple.com/us/app/propanetracker/id6757357644" target="_blank" rel="noopener" class="store-badge">
					<img src="/app-store-badge.svg" alt="Download on the App Store" />
				</a>
				<a href="https://play.google.com/store/apps/details?id=com.codepasture.propane_tracker&hl=en_US" target="_blank" rel="noopener" class="store-badge">
					<img src="/google-play-badge.png" alt="Get it on Google Play" />
				</a>
			</div>
		</section>

		<section class="section">
			<h2>The Problem</h2>
			<p>You check your propane tank gauge, make a mental note, and promptly forget. Without a record of your readings, it's hard to spot trends or remember what your usage looked like last winter. Propane consumption varies with weather, so having historical data helps you make better decisions about when to schedule deliveries.</p>
		</section>

		<section class="section">
			<h2>Features</h2>
			<div class="features-grid">
				<div class="feature">
					<h3>Tank Gauge Readings</h3>
					<p>Log readings from your tank gauge (0-100%). Add the date, temperature, and notes. Build a history of your tank levels over time.</p>
				</div>
				<div class="feature">
					<h3>Delivery Tracking</h3>
					<p>Record deliveries with gallons, total cost, and before/after tank levels. The app calculates your price per gallon automatically.</p>
				</div>
				<div class="feature">
					<h3>Consumption Statistics</h3>
					<p>See gallons per day broken down by month and year. Understand how your usage changes with seasons and weather.</p>
				</div>
				<div class="feature">
					<h3>Depletion Estimates</h3>
					<p>Based on recent consumption, the app estimates days until 20%. These are rough guides - take more frequent readings as weather changes.</p>
				</div>
				<div class="feature">
					<h3>Visual Tank Gauge</h3>
					<p>Color-coded display: green (above 35%), orange (20-35%), red (below 20%). Know your status at a glance.</p>
				</div>
				<div class="feature">
					<h3>Delivery History</h3>
					<p>12-month view of all deliveries with total gallons, total cost, and average price per gallon. Track spending trends.</p>
				</div>
				<div class="feature">
					<h3>CSV Export & Import</h3>
					<p>Export readings, deliveries, and configuration to CSV. Import to restore or transfer data. Your records, portable format.</p>
				</div>
				<div class="feature">
					<h3>Offline-First</h3>
					<p>All data stored locally on your device. No account required, no cloud sync needed. Works anywhere, even at the tank.</p>
				</div>
			</div>
		</section>

		<section class="section">
			<h2>Built With</h2>
			<p>Propane Tracker is a Flutter app built with Dart, following clean architecture with domain-driven design. The domain layer is pure Dart with zero Flutter dependencies, making business logic fully testable. It uses Riverpod for state management and SQLite for local persistence.</p>
		</section>

		<section class="section cta">
			<h2>Need a Custom Mobile App?</h2>
			<p>Code Pasture builds Flutter and React Native apps for businesses. Utility monitoring, IoT integrations, field service tools, we turn complex requirements into simple mobile experiences. 30 years of full-stack experience, from first commit to App Store.</p>
			<a href="/#contact" class="cta-link">Get in Touch &rarr;</a>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/propane-tracker/support">Support</a> &middot; <a href="/propane-tracker/privacy">Privacy Policy</a>
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

	.store-badge img[src*="google-play"] {
		height: 66px;
		margin: -11px 0;
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

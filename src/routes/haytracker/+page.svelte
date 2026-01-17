<script lang="ts">
</script>

<svelte:head>
	<title>HayTracker - Hay & Straw Inventory for Farms | Code Pasture</title>
	<meta name="description" content="HayTracker is a mobile app for tracking hay and straw inventory on farms. Know when feed will run out with consumption projections and depletion estimates. Built with Flutter by Code Pasture." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<section class="hero">
			<img src="/haytracker-icon.png" alt="HayTracker app icon" class="app-icon" />
			<h1>HayTracker</h1>
			<p class="tagline">Know when the hay runs out before your livestock do</p>
			<div class="store-badges">
				<a href="https://apps.apple.com/us/app/haytracker/id6757104455" target="_blank" rel="noopener" class="store-badge">
					<img src="/app-store-badge.svg" alt="Download on the App Store" />
				</a>
				<a href="https://play.google.com/store/apps/details?id=com.codepasture.haytracker" target="_blank" rel="noopener" class="store-badge">
					<img src="/google-play-badge.png" alt="Get it on Google Play" />
				</a>
			</div>
		</section>

		<section class="section">
			<h2>The Problem</h2>
			<p>Running a small farm means juggling a lot of mental notes. How many bales do we have left? How fast are we going through them? When should we order more? A spreadsheet works until it doesn't. You need something you can update from the barn with cold fingers and a phone in your pocket.</p>
		</section>

		<section class="section">
			<h2>Features</h2>
			<div class="features-grid">
				<div class="feature">
					<h3>Three-State Hay Tracking</h3>
					<p>Track bales through their lifecycle: Stock (in storage), In Use (being fed), and Consumed (finished). See exactly what's available.</p>
				</div>
				<div class="feature">
					<h3>Straw Inventory</h3>
					<p>Separate tracking for bedding straw with a simpler two-state workflow. Keep hay and straw inventories organized but distinct.</p>
				</div>
				<div class="feature">
					<h3>Consumption Projections</h3>
					<p>See bales per day and estimated depletion dates. The app calculates when you'll run out based on actual usage patterns.</p>
				</div>
				<div class="feature">
					<h3>Urgency Indicators</h3>
					<p>Clear visual warnings: critical (less than 7 days), warning (7-30 days), or OK (more than 30 days). Know at a glance if you need to act.</p>
				</div>
				<div class="feature">
					<h3>Delivery Tracking</h3>
					<p>Log deliveries with cost per bale, delivery fees, and notes about cutting quality. Track spending over time.</p>
				</div>
				<div class="feature">
					<h3>Standard Bale Types</h3>
					<p>Pre-loaded with industry-standard sizes: small/large square bales, 4x4, 4x5, 5x5 round bales. Add custom types for non-standard sizes.</p>
				</div>
				<div class="feature">
					<h3>CSV Export & Import</h3>
					<p>Export your data for records or backup. Import to restore or migrate. Your data, your format.</p>
				</div>
				<div class="feature">
					<h3>Offline-First</h3>
					<p>Works without cell service. All data stored locally on your device. Update inventory from anywhere on the property.</p>
				</div>
			</div>
		</section>

		<section class="section">
			<h2>Built With</h2>
			<p>HayTracker is a Flutter app built with Dart, following clean architecture principles with domain-driven design. It uses Riverpod for state management and SQLite for local persistence. The codebase serves as an architectural template demonstrating enterprise-grade patterns in a mobile context.</p>
		</section>

		<section class="section cta">
			<h2>Need a Custom Mobile App?</h2>
			<p>Code Pasture builds Flutter and React Native apps for businesses. Agricultural tech, inventory management, field service apps, we turn domain expertise into mobile tools. 30 years of full-stack experience, from first commit to App Store.</p>
			<a href="/#contact" class="cta-link">Get in Touch &rarr;</a>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/haytracker/support">Support</a> &middot; <a href="/haytracker/privacy">Privacy Policy</a>
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

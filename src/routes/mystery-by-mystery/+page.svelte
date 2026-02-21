<script lang="ts">
</script>

<svelte:head>
	<title>Mystery by Mystery - A Catholic Rosary Companion | Code Pasture</title>
	<meta name="description" content="Mystery by Mystery is a beautiful, simple Catholic Rosary companion app for iOS, macOS, Android, Windows, and Linux. Pray the complete Rosary with scripture, track your progress, and build a daily prayer habit." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<section class="hero">
			<img src="/mystery-by-mystery-icon.png" alt="Mystery by Mystery app icon" class="app-icon" />
			<h1>Mystery by Mystery</h1>
			<p class="tagline">A Catholic Rosary companion for daily prayer</p>
			<!-- Store badges: uncomment when App Store / Google Play URLs are available
			<div class="store-badges">
				<a href="https://apps.apple.com/us/app/mystery-by-mystery/idXXXXXXXXXX" target="_blank" rel="noopener" class="store-badge">
					<img src="/app-store-badge.svg" alt="Download on the App Store" />
				</a>
				<a href="https://play.google.com/store/apps/details?id=com.codepasture.mystery_by_mystery" target="_blank" rel="noopener" class="store-badge">
					<img src="/google-play-badge.png" alt="Get it on Google Play" class="google-play" />
				</a>
			</div>
			-->
		</section>

		<section class="section">
			<h2>Simple, Beautiful Prayer</h2>
			<p>Mystery by Mystery helps you pray the Rosary with focus and intention. Know which mysteries are for today, read the scripture for each decade, and track where you are — all in a clean, distraction-free experience with no ads and no account required.</p>
		</section>

		<section class="section">
			<h2>Features</h2>
			<div class="features-grid">
				<div class="feature">
					<h3>All Four Mystery Sets</h3>
					<p>Joyful, Sorrowful, Glorious, and Luminous mysteries with full scripture passages for every decade.</p>
				</div>
				<div class="feature">
					<h3>Daily Default or Continuous Cycle</h3>
					<p>Default to the traditional mystery for each day, or pray through all the sets in order. Switch mystery sets at any time.</p>
				</div>
				<div class="feature">
					<h3>Decade-by-Decade Progress</h3>
					<p>Track your place through the Rosary with a visual bead indicator. Pick up right where you left off.</p>
				</div>
				<div class="feature">
					<h3>Scripture Readings</h3>
					<p>Each mystery includes its scripture passage in both the CPDV and Douay-Rheims translations.</p>
				</div>
				<div class="feature">
					<h3>Prayer History</h3>
					<p>See your completed Rosaries over time. Build a habit and watch your prayer life grow.</p>
				</div>
				<div class="feature">
					<h3>Collapsible Prayers</h3>
					<p>Opening prayers, decade prayers, and closing prayers are collapsible so you can focus on what you need.</p>
				</div>
				<div class="feature">
					<h3>No Account Required</h3>
					<p>Everything is stored locally on your device. No sign-up, no cloud sync, no tracking. Just prayer.</p>
				</div>
				<div class="feature">
					<h3>Every Platform</h3>
					<p>Available on iOS, macOS, Android, Windows, and Linux. The same beautiful experience everywhere.</p>
				</div>
			</div>
		</section>

		<section class="section">
			<h2>Built With</h2>
			<p>Mystery by Mystery is built with Flutter for all platforms. Riverpod for state management, SQLite for local persistence. All prayer data and scripture is bundled with the app — no internet connection needed to pray.</p>
		</section>

		<section class="section cta">
			<h2>Need a Custom Mobile App?</h2>
			<p>Code Pasture builds React Native and Flutter apps for businesses. From time tracking to inventory management to IoT monitoring, we turn ideas into production apps. 30 years of full-stack experience, from first commit to App Store.</p>
			<a href="/#contact" class="cta-link">Get in Touch &rarr;</a>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/mystery-by-mystery/support">Support</a> &middot; <a href="/mystery-by-mystery/privacy">Privacy Policy</a>
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

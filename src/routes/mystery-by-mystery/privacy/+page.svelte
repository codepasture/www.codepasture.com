<script lang="ts">
</script>

<svelte:head>
	<title>Mystery by Mystery Privacy Policy | Code Pasture</title>
	<meta name="description" content="Privacy policy for Mystery by Mystery, a Catholic Rosary companion app for iOS, macOS, Android, Windows, and Linux." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<h1>Mystery by Mystery Privacy Policy</h1>
		<p class="effective-date">Effective Date: February 21, 2026</p>

		<section class="section">
			<h2>Overview</h2>
			<p>
				Mystery by Mystery is a local-first prayer app. We do not operate any servers, collect any data, or have access to your prayer history. All information stays on your device.
			</p>
		</section>

		<section class="section">
			<h2>Data Storage</h2>
			<p>
				All prayer history, session progress, and settings are stored locally on your device in a SQLite database. No data is stored on Code Pasture servers. The app works entirely offline — no internet connection is required to pray.
			</p>
		</section>

		<section class="section">
			<h2>Data Collection</h2>
			<p>
				Mystery by Mystery does not collect any data. Specifically:
			</p>
			<ul>
				<li>No personal information is collected</li>
				<li>No usage analytics or tracking</li>
				<li>No location data</li>
				<li>No device identifiers sent to us</li>
				<li>No crash reports or telemetry</li>
				<li>No third-party analytics services</li>
				<li>No advertising networks</li>
			</ul>
		</section>

		<section class="section">
			<h2>In-App Purchases</h2>
			<p>
				Mystery by Mystery offers optional donation-based in-app purchases. These transactions are processed entirely by Apple (App Store) or Google (Google Play). Code Pasture does not receive or store any payment information, credit card numbers, or billing details. We only receive confirmation that a purchase was made so the app can display your supporter status.
			</p>
		</section>

		<section class="section">
			<h2>Data Backup</h2>
			<p>
				Your Mystery by Mystery data may be included in your device's standard backup process (iCloud, Google Drive, or local backups). These backups are managed by the platform provider and are subject to their respective privacy policies.
			</p>
		</section>

		<section class="section">
			<h2>Data Retention and Deletion</h2>
			<p>
				Your data remains on your device until you choose to delete it. You can clear your prayer history within the app, or uninstall the app to remove all associated data. We have no ability to access, retain, or delete your data as it exists only on your device.
			</p>
		</section>

		<section class="section">
			<h2>Children's Privacy</h2>
			<p>
				Mystery by Mystery does not collect any information from anyone, including children under the age of 13.
			</p>
		</section>

		<section class="section">
			<h2>Changes to This Policy</h2>
			<p>
				We may update this privacy policy from time to time. Any changes will be posted on this page with an updated effective date. Significant changes will be noted in the app's update notes on the App Store and Google Play Store.
			</p>
		</section>

		<section class="section">
			<h2>Contact</h2>
			<p>
				If you have any questions about this privacy policy, please contact us at:
			</p>
			<a href="mailto:mystery-by-mystery@codepasture.com" class="email-link">mystery-by-mystery@codepasture.com</a>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/mystery-by-mystery/support">Support</a>
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
		margin-bottom: 0.5rem;
	}

	.effective-date {
		color: var(--color-text-muted);
		font-size: 0.9rem;
		margin-bottom: 2rem;
	}

	.section {
		margin-bottom: 2rem;
	}

	.section h2 {
		font-size: 1.25rem;
		font-weight: 600;
		margin-bottom: 0.75rem;
		color: var(--color-accent);
	}

	.section p {
		color: var(--color-text-muted);
		line-height: 1.7;
	}

	.section ul {
		color: var(--color-text-muted);
		line-height: 1.8;
		padding-left: 1.5rem;
		margin-top: 0.5rem;
	}

	.section li {
		margin-bottom: 0.25rem;
	}

	.email-link {
		display: inline-block;
		margin-top: 0.5rem;
		font-size: 1.1rem;
		font-weight: 500;
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
